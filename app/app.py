"""
Task: https://app.swaggerhub.com/apis/c4412/croc-gamification/1.0.0#/auction/addAuctionState
"""

from argparse import Action
from urllib import request
from fastapi import FastAPI, Depends
from app.shemas import *
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database import engine
from app.database import get_db
from app.models import *
from random import randint
import json


Base.metadata.create_all(bind=engine)
app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.post("/auction")
# async def add_auction(details: CreateAuction, db: Session = Depends(get_db)):
#     q = db.query(Auction).all()[-1]
#     new_auction = Auction(
#         auction_id=q.auction_id + 1,
#         auction=json.loads(details.json()),
#     )
#     db.add(new_auction)
#     db.commit()
#
#     return {"status": "Ok"}
#
#
# @app.get("/auction/{auctionId}")
# async def get_auction(auctionId: int, db: Session = Depends(get_db)):
#     stmt = select(Auction).where(Auction.auction_id == auctionId)
#     result = db.execute(stmt).scalar_one_or_none()
#     if result:
#         return json.loads(result.auction)
#     return {"status": "auction not found"}
#
#
# @app.delete("/auction/{auctionId}")
# async def delete_auction(auctionId: int, db: Session = Depends(get_db)):
#     stmt = select(Auction).where(Auction.auction_id == auctionId)
#     result = db.execute(stmt).scalar_one_or_none()
#     if result:
#         db.delete(result)
#         db.commit()
#         return {"status": f"auction with id:{auctionId} deleted"}
#     return {"status": f"{auctionId} not Found"}
#
#
# @app.get("/auctions")
# async def get_all_auctions(db: Session = Depends(get_db)):
#     stmt = select(Auction)
#     query = db.execute(stmt).scalars().all()
#     result = []
#     for auction in query:
#         result.append(json.loads(auction.auction))
#     return result
#
#
# @app.post("/settings")
# async def set_settings(details: GetSettings, db: Session = Depends(get_db)):
#     stmt = select(Setting).where(Setting.settings_id == 1)
#     settings = db.execute(stmt).scalar_one_or_none()
#     if settings:
#         print(settings)
#         settings.settings_json = json.loads(details.json())
#         db.commit()
#         return {"status": "settings was updated!"}
#     else:
#         print(details)
#         settings = Setting(settings_id=1, settings_json=json.loads(details.json()))
#         db.add(settings)
#         db.commit()
#         return {"status": "added new settings"}
#
#
# @app.get("/settings")
# async def get_settings(db: Session = Depends(get_db)):
#     stmt = select(Setting).where(Setting.settings_id == 1)
#     settings = db.execute(stmt).scalar_one_or_none()
#     if settings:
#         return settings.settings_json
#     else:
#         return {"status": "settings no found"}
#
#
# @app.get("/compute-wheel")
# async def compute_wheel(details: ComputeWheel, db: Session = Depends(get_db)):
#     stmt = select(Setting).where(Setting.settings_id == 1)
#     settings = db.execute(stmt).scalar_one_or_none()
#     if settings:
#         exchangeRate = settings.settings_json["exchangeRate"]
#         print(details.computationBudget)
#         response = details.compute(exchangeRate)
#         return response
#     else:
#         return {"status": "settings no found"}
#
#     return json.loads(response.json())
#
#
# @app.post("wheel/lots")
# async def save_wheel_lots(details: WheelLots, db: Session = Depends(get_db)):
#     new_id = db.query(Lot).all()[-1].lot_id
#     if new_id:
#         new_id = +1
#     else:
#         new_id = 0
#     new_calculation = Lot(lot_id=new_id, json_data=json.loads(details.json()))
#     db.add(new_calculation)
#     db.commit()
#     return {"status": 200}
#
#
# @app.post("wheel/lots/{wheelId}")
# async def save_wheel_lots(wheelId: int, db: Session = Depends(get_db)):
#     stmt = select(Lot).where(Lot.lot_id == wheelId)
#     result = db.execute(stmt).scalar_one_or_none()
#     if result:
#         return json.loads(result.json_data)
#     return {"status": "auction not found"}
#
#
# @app.delete("wheel/lots/{wheelId}")
# async def delete_wheel_lots(wheelId: int, db: Session = Depends(get_db)):
#     stmt = select(Lot).where(Lot.lot_id == wheelId)
#     result = db.execute(stmt).scalar_one_or_none()
#     if result:
#         db.delete(result)
#         db.commit()
#         return {"status": f"wheel calculation with id:{wheelId} deleted"}
#     return {"status": f"{wheelId} not Found"}
#
#
# @app.get("/wheel-lots")
# async def get_all_lots(db: Session = Depends(get_db)):
#     stmt = select(Lot)
#     query = db.execute(stmt).scalars().all()
#     result = []
#     for lot in query:
#         result.append(json.loads(lot.json_data))
#     return result


# docker container rm crocapp && docker build -t crocback . && docker run --name crocapp -p 80:80 crocback
