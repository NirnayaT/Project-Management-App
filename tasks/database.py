from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker


# Establish a connection to the PostgreSQL database
engine = create_engine("postgresql://postgres:admin123@localhost:5432/todoapp")

connection = engine.connect()

Base = declarative_base()


class Task(Base):  # main class table
    __tablename__ = "tasks"  # table name
    id = Column(Integer(), primary_key=True)
    task = Column(String(100), nullable=False)
    is_complete = Column(String(10), nullable=False, default=False)
    created_on = Column(DateTime(), default=datetime.now)


Base.metadata.create_all(engine)  # create engine

Session = sessionmaker(bind=engine)
session = Session()  # session starts
