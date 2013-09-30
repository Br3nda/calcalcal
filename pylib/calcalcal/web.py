import time
import calcalcal
def year_from_today():
    return {
        '03': 3,
        '04': 2,
        '05': 13,
        '06': 2,
        '07': 23,
        '08': 2,
        '09': 23,
        '10': 2,
        '11': 0,
        '12': 34,
        '01': 23,
        '02': 0}

def get_events():
    today = time.time()
    
    events_today = [] 
    for e in calcalcal.get_events(today, today):
      events_today.append({'id': e.id, 'name': e.name})

    return {'Today': events_today,
        'This Month': [],
        'April': []
        }