from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from .loader import Base


class Journal(Base):
    __tablename__ = "journal"
    id = Column(Integer, primary_key=True, autoincrement=True)
    flight = Column(Integer, ForeignKey("flight.id"))
    currentTask = Column(Integer)
    bus_id = Column(Integer, ForeignKey("bus.id"))


class Flight(Base):
    __tablename__ = "flight"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    date = Column(Integer)
    type = Column(String)  # A - прилет, D - вылет
    terminal = Column(String)
    companyName = Column(String)
    scheduledTime = Column(Integer)
    airportCode = Column(String)
    airport = Column(String)
    planeType = Column(String)
    parkingId = Column(String)
    gateId = Column(String)
    passengersCount = Column(Integer)

    # journal = relationship("Task")


class Bus(Base):
    __tablename__ = "bus"
    id = Column(Integer, primary_key=True, autoincrement=True)
    capacity = Column(Integer)
    point = Column(String)
    state = Column(String)


class Road(Base):
    __tablename__ = "road"
    id = Column(Integer, primary_key=True)
    sourceId = Column(Integer)
    targetId = Column(Integer)
    distance = Column(Integer)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    journal = Column(Integer, ForeignKey("journal.id"))
    # taskState = Column(String)
    busState = Column(String)
    distance = Column(Integer)  # метры
    startPoint = Column(Integer)  # Integer -> String
    endPoint = Column(Integer)  # Integer -> String


class Point(Base):
    __tablename__ = "points"
    pointId = Column(Integer)
    locationId = Column(String, primary_key=True)
