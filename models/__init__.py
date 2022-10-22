from .models import *
from .loader import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)
