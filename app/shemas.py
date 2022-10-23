from pydantic import BaseModel, Json, Field
from time import time


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
    journal: int
    taskState: str
    busStat: str
    bus_id: int
    distance: int
    startPoint: int
    endPoint: str
