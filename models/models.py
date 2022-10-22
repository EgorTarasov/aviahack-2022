from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from loader import Base


class Journal(Base):
    __tablename__ = "journal"
    id = Column(Integer, primary_key=True)
    flight = Column(Integer, ForeignKey("flight.number"))
    currentTask = Column(Integer)


class Flight(Base):
    __tablename__ = "flight"
    number = Column(Integer, primary_key=True)
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
    id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    state = Column(String)


class Road(Base):
    __tablename__ = "road"
    id = Column(Integer, primary_key=True)
    sourceId = Column(Integer)
    targetId = Column(Integer)
    distance = Column(Integer)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    journal = Column(Integer, ForeignKey("journal.id"))
    taskState = Column(String)
    busState = Column(String)
    bus_id = Column(Integer, ForeignKey("bus.id"))
    distance = Column(Integer)  # метры
    startPoint = Column(Integer)  # id точки начала
    endPoint = Column(Integer)


class Point(Base):
    __tablename__ = "points"
    pointId = Column(String, primary_key=True)
    locationId = Column(String)
