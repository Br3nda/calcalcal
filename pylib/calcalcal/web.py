import datetime
import calendar
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
  
    #TODAY
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    
    events_today = [] 
    for e in calcalcal.get_events(today, (today + one_day) ):
      events_today.append(format_event(e))
      
      
    #This month
    last_day_of_month = calendar.monthrange(today.year ,today.month)[1]
    first_of_month = today.replace(day=1)
    end_of_month = today.replace(day=last_day_of_month)    
    events_this_month = []
    for e in calcalcal.get_events(first_of_month, end_of_month):
      events_this_month.append(format_event(e))

    #Next month
    first_of_next_month = add_months(first_of_month, 1)
    last_day_of_next_month = calendar.monthrange(first_of_next_month.year, first_of_next_month.month)[1]
    last_of_next_month = first_of_next_month.replace(day=last_day_of_next_month)
    events_next_month = []
    for e in calcalcal.get_events(first_of_next_month, last_of_next_month):
      events_next_month.append(format_event(e))
    
    print first_of_next_month.month
    next_month_name = first_of_next_month.strftime('%B')
    return {
	'today': events_today,
        'this_month': events_this_month,
        'next_month': events_next_month,
        'next_month_name': next_month_name
        }

def format_event(e):
  return {'id': e.id, 'name': e.name, 'group': e.group, 'location': e.location}
    
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    added_months = datetime.date(year, month, day)    
    return added_months