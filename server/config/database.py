from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DATABASE_URL = config("DATABASE_URL")
# Establish a connection to the PostgreSQL database
engine = create_engine(DATABASE_URL)

connection = engine.connect()


Base = declarative_base()


Base.metadata.create_all(engine)  # create engine

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()  # session starts


