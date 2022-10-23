from pydantic import BaseModel, Json, Field
from typing import Optional


class BusSchema(BaseModel):
    id: int
    capacity: int
    state: str

    class Config:
        orm_mode = True


class FlightSchema(BaseModel):

    id: int
    number: int
    date: int
    type: str
    terminal: str
    companyName: str
    scheduledTime: int
    airportCode: str
    airport: str
    planeType: str
    parkingId: str
    gateId: str
    passengersCount: int

    class Config:
        orm_mode = True


class TaskScheme(BaseModel):
    id: int
    flight_id: int
    startTime: int
    endTime: Optional[int]
    bus_id: int
    distance: int
    startPoint: int
    endPoint: int

    class Config:
        orm_mode = True
