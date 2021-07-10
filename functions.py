import datetime as dt

def get_end_date(start_date, time_delta):
    return start_date + time_delta

def get_current_day(start_date):
    if start_date > dt.date.today():
        return dt.timedelta(days=0)
    else:
        return dt.date.today() - start_date + dt.timedelta(days=1)

def get_days_left(start_date, time_delta):
    return time_delta - get_current_day(start_date)