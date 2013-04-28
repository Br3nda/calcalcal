from calcalcal.db import Event, DB

def get_events(start, end):
    return DB.query(Event)\
        .filter_by(Event.date_start >= start)\
        .filter_by(Event.date_end <= end)
   

def populate_data():
    Event(name='DesignPro')
    Event(name='Creative Skills')
    Event(name='Design & Thinking') 