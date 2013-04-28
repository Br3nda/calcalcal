from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('pgsql://evencal@eventcal:', echo=True)
Base = declarative_base()

from sqlalchemy.orm import sessionmaker
DB = sessionmaker(bind=engine)
print DB

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ical_url = Column(String)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date_start = Column(Integer)

    
    


Base.metadata.create_all(engine) 