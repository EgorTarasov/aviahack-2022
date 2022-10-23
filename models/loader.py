from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://test_user:test_password@127.0.0.1:5432/test2"
#"postgresql://test_user:test_password@94.45.223.241:46873/test2"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base = declarative_base()
