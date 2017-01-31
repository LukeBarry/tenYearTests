from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime


from . import app

engine = create_engine(app.config["DATABASE_URL"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    student_id = Column(String(1024))
    student_name = Column(String(1024))
    parent_name = Column(String(1024))
    site_location = Column(String(1024))  
    phone_number = Column(String(1024)) 
    alt_number = Column(String(1024)) 
    notes = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)
    
# Base.metadata.drop_all(engine) # learn about migrations
Base.metadata.create_all(engine)

