from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
def recreate_database():
    pass
    
  
class Group(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    
    
    
    
def populate_data():
    Event(name='DesignPro')
    Event(name='Creative Skills')
    Event(name='Design & Thinking')
