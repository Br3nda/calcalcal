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
    today = time.gmtime()
    events_today = calcalcal.get_events(today, today)
    return {'Today': events_today,
        'This Month': [],
        'April': []
        }