from app.app import app
import uvicorn
from app.models import Base
from app.database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app)