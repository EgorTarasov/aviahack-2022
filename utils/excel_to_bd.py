from datetime import datetime
import pandas as pd
from models import *
from sqlalchemy import select
import random
import datetime


def main():
    Session = SessionLocal()
    # initializing SqlAlchemy
    df = pd.read_excel("flights.xlsx", sheet_name="Лист1")
    for index, row in df.iterrows():
        (
            date,
            _type,
            terminal,
            aviaCode,
            number,
            scheduled_time,
            airportCode,
            airportName,
            aircraftType,
            parkingId,
            gateId,
            passengersCount,
        ) = row
        day, mounth, year = [int(i) for i in date.split(".")]
        hour, minutes = scheduled_time.hour, scheduled_time.minute
        date = datetime.datetime(
            year=year, month=mounth, day=day, hour=hour, minute=minutes
        )

        unix_timestamp = datetime.datetime.timestamp(date)*1000

        f = Flight(
            number=number,
            date=unix_timestamp,
            type=_type,
            terminal=terminal,
            companyName=aviaCode,
            scheduledTime=unix_timestamp,
            airportCode=airportCode,
            airport=airportName,
            planeType=aircraftType,
            parkingId=parkingId,
            gateId=gateId,
            passengersCount=passengersCount,
        )
        Session.add(f)
        Session.flush()

    df = pd.read_excel("points.xlsx", sheet_name="Points")
    c = 0
    values = []
    for index, row in df.iterrows():
        pointId, locationId = row
        locationId = str(locationId)
        values.append((pointId, locationId))
        c += 1
        point = Session.query(Point).filter_by(
            locationId=locationId).one_or_none()
        if point is None:
            point = Point(pointId=pointId, locationId=locationId)
        Session.add(point)
        Session.flush()

    df = pd.read_excel("points.xlsx", sheet_name="Roads")
    for index, row in df.iterrows():
        road_id, source_point_id, target_point_id, distance = row
        road = Session.query(Road).filter_by(id=road_id).one_or_none()
        if road is None:
            road = Road(
                id=road_id,
                sourceId=source_point_id,
                targetId=target_point_id,
                distance=distance,
            )
        Session.add(road)
        Session.flush()


def place_busses():
    capacity = {
        50: 20,
        100: 30,
    }
    Session = SessionLocal()
    points = Session.query(Point).all()
    _id = 1
    for k in capacity.keys():
        print(k, capacity)
        for n in range(capacity[k]):
            bus_id = _id
            _capacity = k
            bus = Session.query(Bus).filter_by(id=bus_id).one_or_none()
            point = random.choice(points)
            if bus is None:
                bus = Bus(
                    id=bus_id, capacity=_capacity, state=True, point=point.pointId
                )

            Session.add(bus)
            _id += 1
        Session.flush()


if __name__ == "__main__":
    main()
    place_busses()
