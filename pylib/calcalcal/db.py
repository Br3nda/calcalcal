from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('postgresql://eventcal@localhost:5432/eventcal', echo=True)
Base = declarative_base()

from sqlalchemy.orm import sessionmaker
DB = sessionmaker(bind=engine)
print DB
DBSession = DB()

class Group(Base):
    __tablename__ = 'groups'
    id = Column('id', Integer, Sequence('group_id_seq'), primary_key=True)
##    id = Column(Integer, primary_key=True)
    name = Column(String)
    ical_url = Column(String)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date_start = Column(Integer)
    date_end = Column(Integer)
    
    

Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine) 


import datetime

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
DBSession.add(Event(name='DesignPro', date_start=today.toordinal(), date_end = (today + one_day).toordinal()))
DBSession.add(Event(name='Creative Skills', date_start=today.toordinal()))
DBSession.add(Event(name='Design & Thinking', date_start=today.toordinal()) )