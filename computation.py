from models import *
from sqlalchemy import desc
import asyncio


class Controller:
    def __init__(self) -> None:
        Session = SessionLocal()
        # loop = asyncio.get_event_loop()
        # if loop is None:
        #     loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        self.flights: list[Flight] = (
            Session.query(Flight).order_by(desc(Flight.scheduledTime)).all()
        )
        print(self.flights)
        return None

    def get_journals(self) -> list[Journal]:
        Session = SessionLocal()
        result: list[Task] = []
        for f in Flight:
            j_id = len(Session.query(Journal).all()) + 1
            if f.type == "A":  # Прилет
                startPoint = Session.query(Point).where(locationId=f.parkingId).one()
                endPoint = Session.query(Point).where(locationId=f.gateId).one()
            elif f.type == "D":
                endPoint = Session.query(Point).where(locationId=f.parkingId).one()
                startPoint = Session.query(Point).where(locationId=f.gateId).one()
            t1 = Task(journal=j_id, busState="boarding")
            t2 = Task(
                startPoint=startPoint,
                endPoint=endPoint,
                busState="busy",
                distance=Controller.compute_distance(startPoint, endPoint),
            )
            t3 = Task(busState="unboarding")

            Controller._find_bus(f.parkingId)
            pass

    @staticmethod
    def compute_distance(startPoint: int, endPoint: int):
        return 10

    @staticmethod
    def _find_bus(locationId: str, _except: tuple[Bus] = ()):
        return Bus


def main():
    controller = Controller()
    print(controller.get_journals())


if __name__ == "__main__":
    main()
