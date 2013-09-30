import datetime
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
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    
    events_today = [] 
    for e in calcalcal.get_events(today, (today + one_day) ):
      events_today.append({'id': e.id, 'name': e.name})
      
      
    import calendar
    last_day_of_month = calendar.monthrange(today.year ,today.month)[1]
    first_of_month = today.replace(day=1)
    end_of_month = today.replace(day=last_day_of_month)    
    events_this_month = []
    for e in calcalcal.get_events(first_of_month, end_of_month):
      events_this_month.append({'id': e.id, 'name': e.name})

    return {
	'today': events_today,
        'this_month': events_this_month,
        'next_month': []
        }