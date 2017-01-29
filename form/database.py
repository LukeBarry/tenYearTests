from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime


from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Entry(Base):
    __tablename__ = "entries"

    student_id = Column(String, primary_key=True)
    student_first_name = Column(String(1024))
    student_last_name = Column(String(1024))
    parent_first_name = Column(String(1024))
    parent_last_name = Column(String(1024))
    site_location = Column(String(1024))   
    phone_number = Column(Integer)
    alt_number = Column(Integer)
    notes = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)
    

Base.metadata.create_all(engine)

