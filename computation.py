import datetime
import time

from models import *

from sqlalchemy import desc


class Controller:
    def __init__(self) -> None:
        session = SessionLocal()
        # loop = asyncio.get_event_loop()
        # if loop is None:
        #     loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
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

            if start_point is None or end_point is None:
                not_found.append((f.parkingId, f.gateId))
                continue
            start_point, end_point = start_point.pointId, end_point.pointId
            distance, duration = Controller.compute_distance(startPoint=start_point,endPoint=end_point)
            t = Task(
                bus_id=Controller._find_bus(start_point),
                flight_id=f.id,
                distance=distance,
                startPoint=start_point,
                endPoint=end_point,
                startTime=int(time()),
                duration=duration,

            )
            bus = session.query(Bus).filter_by(id=t.bus_id).one_or_none()
            if bus is None:
                raise Exception("Автобуса не существует")
            bus.state=False
            session.add(bus)
            session.add(t)
            session.flush()

            result.append(
                TaskScheme(
                    id=t.id,
                    bus_id=t.bus_id,
                    bus_capacity=session.query(Bus).filter_by(id=t.bus_id).one().capacity,
                    duration=t.duration,
                    distance=t.distance,
                    startPoint=start_point_scheme,
                    endPoint=end_point_scheme,
                )
            )


        # FIXME: Это не смогло найти мб изменить запрос sql
        print(len(not_found), not_found)
        return result

    @staticmethod
    def compute_distance(startPoint: int, endPoint: int) -> (int, int):
        # TODO: прикрутить расчет Егора
        # TODO: прикрутить
        # tuple формата дистанция, время выполнение
        return (10, 100)

    @staticmethod
    def _find_bus(locationId: str, _except: tuple[Bus] = ()) -> int:
        # TODO: прикрутить расчет Егора
        return 1


def main():
    controller = Controller()
    controller.get_journals()


if __name__ == "__main__":
    main()
