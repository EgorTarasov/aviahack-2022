"""
Task: https://app.swaggerhub.com/apis/c4412/croc-gamification/1.0.0#/auction/addAuctionState
"""
from unittest import result
from fastapi import FastAPI, Depends
from app.shemas import *
from sqlalchemy import select
from fastapi import APIRouter
from models import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

CAPACITY = (10, 50, 100)

router_bus = APIRouter()

# TODO bus counter
# TODO all bus (для переназначения)
# TODO post change bus in task


@router_bus.get("/bus_counter")
async def get_bus_count():
    db = SessionLocal()
    answer = {}

    for cap in CAPACITY:
        answer[cap] = {}
        q_free = select(Bus).filter(Bus.state == "waiting")
        q_busy = select(Bus).filter(
            Bus.state != "waiting" and Bus.state != "failed")
        q_failed = select(Bus).filter(Bus.state == "failed")
        answer[cap]["free"] = len(db.execute(q_free).all())
        answer[cap]["busy"] = len(db.execute(q_busy).all())
        answer[cap]["failed"] = len(db.execute(q_failed).all())

    return answer


@router_bus.get("/free")
async def get_free_busses():
    db = SessionLocal()
    busses = [BusScheme(i) for i in db.query(Bus).filter_by(state=True)]
    return busses


@router_bus.get("/all")
async def get_bus_all():
    # Tested
    db = SessionLocal()
    busses = db.execute(select(Bus)).all()
    result = []
    for b in busses:
        result.append(dict(b)["Bus"])
    return result


#
@router_bus.get("/tasks/{bus_id}")
async def get_task(bus_id: int):
    # Tested
    db = SessionLocal()
    result = db.query(Task).filter_by(bus_id=bus_id).all()
    return result


app.include_router(router_bus, prefix="/bus", tags=["bus"])


router_flight = APIRouter()


@router_flight.get("/all")
async def get_all():
    # Tested
    result = []
    Session = SessionLocal()
    query = Session.query(Flight).all()
    
        
    for entity in query:
        a = {}
        tasks = []
        
        for i in Session.query(Task).filter_by(flight_id=entity.id).all():
            t = TaskScheme(
                id=i.id,
                bus_id=i.bus_id,
                bus_capacity=Session.query(Bus).filter_by(
                    id=i.bus_id).one().capacity,
                duration=i.duration,
                distance=i.distance,
                startPoint=i.startPoint,
                endPoint=i.endPoint,
            )
            tasks.append(t)

        a["flight"] = FlightSchema.from_orm(entity)
        a["tasks"] = []
        print(len(tasks))
        result.append(a)

    result = [(dict, dict)]
    return result


app.include_router(router_flight, prefix="/flight", tags=["flight"])
