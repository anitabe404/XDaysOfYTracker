import datetime as dt
import functions as fu

if __name__ == '__main__':
    DURATION = dt.timedelta(days=100)
    start_date = dt.date.fromisoformat(input('Enter start date: '))
    end_date = fu.get_end_date(start_date, DURATION)
    current_day = fu.get_current_day(start_date)
    days_remaining = fu.get_days_left(start_date, DURATION)

    print(f'Your start date is {start_date.strftime("%b %d %Y")}')
    print(f'Your end date is {end_date.strftime("%b %d %Y")}')
    print(f'You are currently on Day {current_day.days}')
    print(f'You have {days_remaining.days} days left')