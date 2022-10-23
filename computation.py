import datetime
import time

from models import *

from sqlalchemy import desc

from dijkstar import Graph, find_path


class Controller:
    def __init__(self) -> None:
        session = SessionLocal()
        # loop = asyncio.get_event_loop()
        # if loop is None:
        #     loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        self.graph = Graph()
        road_list = session.query(Road).all()


        for road in road_list:
            self.graph.add_edge(road.sourceId, road.targetId, (road.distance, road.id))
        
        self.flights: list[Flight] = (
            session.query(Flight).order_by(desc(Flight.scheduledTime)).all()
        )

    def get_journals(self) -> list[TaskScheme]:
        session = SessionLocal()
        result: list[TaskScheme] = []
        not_found: list[tuple[str, str]] = []
        for f in self.flights:
            start_point, end_point = 0, 0

            # exit(0)
            if f.type == "A":  # Прилет
                start_point = (
                    session.query(Point)
                    .filter(Point.locationId == f.parkingId)
                    .one_or_none()
                )
                end_point = (
                    session.query(Point)
                    .filter(Point.locationId == f.gateId)
                    .one_or_none()
                )
                start_point_scheme, end_point_scheme = f.parkingId, f.gateId
            elif f.type == "D":
                start_point = (
                    session.query(Point)
                    .filter(Point.locationId == f.gateId)
                    .one_or_none()
                )
                end_point = (
                    session.query(Point)
                    .filter(Point.locationId == f.parkingId)
                    .one_or_none()
                )
                start_point_scheme, end_point_scheme = f.gateId, f.parkingId

            # FIXME: Должно отображать все точки, но иногда не может найти:
            # 12
            # DGA_I
            # 10
            # DGA_I
            # 11
            # DGA_I
            # 12
            # DGA_I
            # 12
            # DGA_I
            # 10
            # DGA_I
            # 13
            # DGA_I
            # 11
            # DGA_I
            bus = None
            _expeption: list[int] = []
            while bus is None:
                try:
                    bus_id=Controller._find_bus(self, start_point.locationId, _expeption)
                    print(bus_id)
                    bus = session.query(Bus).filter_by(id=bus_id).one_or_none()
                    if bus.state:
                        bus.state = False
                        session.add(bus)
                        break
                    if bus is None:
                        _expeption.append(bus_id)
                        continue
                    
                except Exception as e:
                    print(e)
                    exit(0)
            if start_point is None or end_point is None:
                not_found.append((f.parkingId, f.gateId))
                continue
            start_point, end_point = start_point.pointId, end_point.pointId
            distance, duration = Controller.compute_distance(self,
                startPoint=start_point, endPoint=end_point)
            t = Task(
                bus_id=bus_id,
                flight_id=f.id,
                distance=distance,
                startPoint=start_point,
                endPoint=end_point,
                startTime=int(time()),
                duration=duration,
            )
            session.add(t)
            session.flush()

            result.append(
                TaskScheme(
                    id=t.id,
                    bus_id=t.bus_id,
                    bus_capacity=session.query(Bus).filter_by(
                        id=t.bus_id).one().capacity,
                    duration=t.duration,
                    distance=t.distance,
                    startPoint=start_point_scheme,
                    endPoint=end_point_scheme,
                )
            )

        # FIXME: Это не смогло найти мб изменить запрос sql
        print(len(not_found), not_found)
        return result



    def compute_distance(self, startPoint: int, endPoint: int) -> (int, int):
        # TODO: прикрутить расчет Егора
        # TODO: прикрутить
        # tuple формата дистанция, время выполнение
        def cost_func(u, v, edge, prev):
            length, name = edge
            cost = length
            return cost
        # if endPoint in self.graph.items():
        #     pass
        path_to_destination = find_path(
        self.graph, startPoint, endPoint, cost_func=cost_func)
        distance, dtime =  path_to_destination.total_cost, path_to_destination.total_cost/8
        return (distance, dtime)


    def _find_bus(self, locationId: str, _except: list) -> int:
        # TODO: прикрутить расчет Егора
        session = SessionLocal()
        point_locId = session.query(Point).filter_by(locationId=locationId).one_or_none()
        if point_locId is None:
            raise Exception("Something went wrong(")
        point_locId = point_locId.pointId
        #print(point_locId, type(point_locId))
        
        buses = session.query(Bus).all() # FIXME: Rename buses
        b = 0
        m = self.compute_distance(buses[-1].point, point_locId)[0]
        for i, bus in enumerate(buses):
            if bus.id not in _except:
                length = self.compute_distance(bus.point, point_locId)[0]
                b = bus.id
                #print(length)
                if length <= m and m != 0:
                    m = length
                    b = bus.id
                elif m!= 0:
                    break
        
        return b


def main():
    controller = Controller()
    controller.get_journals()


if __name__ == "__main__":
    main()
