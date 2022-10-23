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

        self.is_operated = True

        self.graph = Graph()
        road_list = session.query(Road).all()

        for road in road_list:
            self.graph.add_edge(road.sourceId, road.targetId,
                                (road.distance, road.id))

        self.flights: list[Flight] = (
            session.query(Flight).order_by(desc(Flight.scheduledTime)).all()
        )

    def warn_operator(self, timee):
        if time.time() - timee > 30: #раз в 30 секунд, если не появились новые рейсы
            # Всплывающее окно с вопросом о завершении работы или просто ожидание нажатия кнопки
            condition = False # обработка соглашения оператора завершенить работу
            if condition:
                self.is_operated = False
            return time.time()
        return timee

    def get_journals(self) -> dict[int: [Task]]:
        session = SessionLocal()
        result = {}
        not_found: list[tuple[str, str]] = []
        self.flights.sort()
        prev_time = -100
        while self.is_operated:
            while len(self.flights) > 0:
                f = self.flights[0]
                result[f.id] = []
                start_point, end_point = 0, 0
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
                if start_point is None or end_point is None:
                    not_found.append((f.parkingId, f.gateId))
                    continue
                bus = None
                _expeption: list[int] = []
                passengers_left = f.passengersCount
                while passengers_left > 0:
                    try:
                        bus_id = Controller._find_bus(
                            self, start_point.locationId, _expeption)
                        bus = session.query(Bus).filter_by(id=bus_id).one_or_none()
                        if bus is None:
                            while bus is None:
                                tasks = session.query(Task).all()
                                tasks.sort()
                            continue
                        if bus.state:
                            bus.state = False
                            passengers_left -= bus.capacity
                            session.add(bus)
                            distance, duration = Controller.compute_distance(
                                self, startPoint=start_point.pointId, endPoint=end_point.pointId,)
                            t = Task(
                                bus_id=bus_id,
                                flight_id=f.id,
                                distance=distance,
                                startPoint=start_point.pointId,
                                endPoint=end_point.pointId,
                                startTime=int(time()),
                                duration=duration,
                            )
                            session.add(t)
                            session.flush()

                            result[f.id].append(
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
                        else:
                            _expeption.append(bus.id)
                            continue

                    except Exception as e:
                        print(e)
                        exit(0)
                self.flights.pop(0)
            prev_time = self.warn_operator(prev_time)
        return result

    def compute_distance(self, startPoint: int, endPoint: int):
        def cost_func(u, v, edge, prev):
            length, name = edge
            cost = length
            return cost

        path_to_destination = find_path(
            self.graph, startPoint, endPoint, cost_func=cost_func)
        distance, dtime = path_to_destination.total_cost, path_to_destination.total_cost//8
        return (distance, dtime)

    def _find_bus(self, locationId: str, _except: list) -> int:
        session = SessionLocal()
        point_locId = session.query(Point).filter_by(
            locationId=locationId).one_or_none()
        if point_locId is None:
            raise Exception("Something went wrong(")
        point_locId = point_locId.pointId

        bus_all = session.query(Bus).all()
        b = 0
        m = self.compute_distance(bus_all[-1].point, point_locId)[0]
        for i, bus in enumerate(bus_all):
            if bus.id not in _except:
                length = self.compute_distance(bus.point, point_locId)[0]
                b = bus.id
                if length <= m and m != 0:
                    m = length
                    b = bus.id
                elif m != 0:
                    break

        return b


def main():
    controller = Controller()
    print(controller.get_journals())


if __name__ == "__main__":
    main()
