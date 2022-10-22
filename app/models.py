from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from .database import Base


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

    journal = relationship("Task")


class Bus(Base):
    __tablename__ = "bus"
    id = Column(Integer, primary_key=True)
    state = Column(String)


class Road(Base):
    __tablename__ = "road"
    id = Column(Integer, primary_key=True)
    sourceId = Column(Integer)
    targetId = Column(Integer)
    distance = Column(Integer)


class BusState(Base):
    __tablename__ = "bus_state"
    id = Column(Integer, primary_key=True)
    label = Column(String)
    duration = Column(Integer)
    order = Column(Integer)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    journal = Column(Integer, ForeignKey("flight.number"))
    taskState = Column(String)
    busState = Column(String)
    bus_id = Column(Integer, ForeignKey("bus.id"))
    distance = Column(Integer)  # метры
    flight = Column(String)
    startPoint = Column(Integer)  # id точки начала
    endPoint = Column(Integer)


class Mission(Base):
    __tablename__ = "missions"

    mission_id = Column(Integer, primary_key=True, nullable=False)
    json_data = Column(postgresql.JSON())
