from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

# from .models import Goal, Task

# TaskSchema = pydantic_model_creator(
#     Task, name="TaskSchema"
# )



class BusStateSchema(BaseModel):
    label: str
    duration: int
    order: int


class BusSchema(BaseModel):
    id: int
    state: bool


class FlightSchema(BaseModel):
    number: int
    date: int
    type: str
    terminal: str
    scheduledTime: int
    airportCode: str
    airport: str
    planeType: str
    parkingId: int
    gateId: str
    passengersCount: int


class PointSchema(BaseModel):
    pointId: int
    locationId: str


class TaskSchema(BaseModel):
    id: int
    bus: BusSchema
    taskState: str
    distance: int
    flight: FlightSchema


class CreateTask(BaseModel):
    text: str
    attachments: str
    complition_date: Optional[int] = None


class DeleteSuccess(BaseModel):
    ok: bool
