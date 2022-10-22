from pydantic import BaseModel, Json, Field
from time import time

class BusSchema(BaseModel):
    id: int
    capacity: int
    state: str

    class Config:
        orm_mode = True
