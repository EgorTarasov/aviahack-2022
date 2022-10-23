from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .loader import Base
from pydantic import BaseModel, Json, Field
from time import time


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    


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

    def __lt__(self, other):
        return self.scheduledTime < other.scheduledTime


class Bus(Base):
    __tablename__ = "bus"
    id = Column(Integer, primary_key=True, autoincrement=True)
    capacity = Column(Integer)
    point = Column(Integer)
    state = Column(Boolean)


class Road(Base):
    __tablename__ = "road"
    id = Column(Integer, primary_key=True)
    sourceId = Column(Integer)
    targetId = Column(Integer)
    distance = Column(Integer)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey("flight.id"))
    startTime = Column(Integer,  nullable=True)
    duration = Column(Integer, nullable=True)
    endTime = Column(Integer, nullable=True)
    bus_id = Column(Integer, ForeignKey("bus.id"))
    distance = Column(Integer)  # метры
    startPoint = Column(Integer)  # Integer -> String
    endPoint = Column(Integer)  # Integer -> String

    def __lt__(self, other):
        return self.startTime + self.duration < other.startTime + other.duration


class Point(Base):
    __tablename__ = "points"
    pointId = Column(Integer)
    locationId = Column(String, primary_key=True)


class TaskScheme(BaseModel):
    id: int
    bus_id: int
    bus_capacity: int
    duration: int
    distance: int
    startPoint: str
    endPoint: str


class BusScheme(BaseModel):
    id: int
    capacity: int
    point: int
    state: str

    class Config():
        orm_mode = True
