from datetime import datetime
import pandas as pd
from models import Base, SessionLocal, engine
from app.models import *
import time
import datetime


def main():
    # initializing SqlAlchemy
    Base.metadata.create_all(bind=engine)
    Session = SessionLocal()
    df = pd.read_excel("data.xlsx", sheet_name="Лист1")
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
        f = Flight(
            number=number,
            date=(time.mktime(date.timetuple())),
            type=_type,
            terminal=terminal,
            companyName=aviaCode,
            scheduledTime=(time.mktime(date.timetuple())),
            airportCode=airportCode,
            airport=airportName,
            planeType=aircraftType,
            parkingId=parkingId,
            gateId=gateId,
            passengersCount=passengersCount,
        )
        Session.add(
            f
        )
        Session.commit()


if __name__ == "__main__":
    main()
