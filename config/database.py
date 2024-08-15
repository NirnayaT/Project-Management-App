from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Establish a connection to the PostgreSQL database
engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/ProjectManagementApp"
)

connection = engine.connect()


Base = declarative_base()


Base.metadata.create_all(engine)  # create engine

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()  # session starts
