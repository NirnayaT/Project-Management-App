from sqlalchemy import create_engine as ce
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# Establish a connection to the PostgreSQL database
engine = ce("postgresql://postgres:admin123@localhost:5432/todoapp")

connection = engine.connect()

Base=declarative_base()

class task(Base): 
    __tablename__='tasks'
    id = Column(Integer(), primary_key=True)
    task=Column(String(100),nullable=False)
    is_complete=Column(String(10),nullable=False, default=False)
    created_on=Column(DateTime(), default=datetime.now)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def show_task():
    details= session.query(task).all()

    for d in details:
        print(d.id,'.',d.task)

def add_task():
    task4=task()
    task4.task=input("Enter the task:")
    session.add(task4.task)
    session.commit()
