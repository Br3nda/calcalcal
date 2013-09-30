from calcalcal.db import Event, DBSEssion

def get_events(start, end):
    return DBSEssion.query(Event)\
		    .filter(Event.date_start >= start)\
		    .filter(Event.date_end <= end)
      
   

