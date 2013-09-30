from calcalcal.db import Event, DBSession

def get_events(start, end):
  
    return DBSession.query(Event)\
		    .filter(Event.date_start >= start.toordinal()) \
		    .filter(Event.date_end <= end.toordinal())
      
   

