import datetime as dt
from challenge_tracker import *
from config_manager import *

def welcome():
    print("===================================================================")
    print("Welcome to the XDaysofY Challenge Tracker")
    print("===================================================================")

def firstRun(config):
    start_date = input('Enter start date in ISO format: ')
    duration = int(input('Enter challenge duration in days: '))
    tracker = ChallengeTracker(start_date, duration)
    config.push(tracker)
    # export tracker to config file
    displayDetails(tracker, config)

def displayDetails(tracker, config):
    print("")
    print("================== Your Challenge Information ====================")
    print(f'Your start date is {tracker.start_date.strftime("%b %d, %Y")}')
    print(f'Your end date is {tracker.end_date.strftime("%b %d, %Y")}')
    print(f'You are currently on Day {tracker.currentDay()}')
    print(f'You have {tracker.remainingDays()} days left')
    print(f'You have missed a total of {tracker.totalMissedDays()} days')
    print("===================================================================")
    print("")
    whatNext(tracker, config)

def whatNext(tracker, config):
    print("-----------------------------------------------------------")
    print("What would you like to do?")
    print("(D)isplay challenge details")
    print("(S)et a day to complete or missed")
    selection = input("> ").upper()
    print("-----------------------------------------------------------")

    if selection == "D":
        displayDetails(tracker, config)
    elif selection == "S":
        setDay(tracker, config)
    else:
        whatNext(tracker, config)

def setDay(tracker, config):
    print("Do you want to:")
    print("(C)omplete a day")
    print("(M)ark a day as missed")
    selection = input("> ").upper()

    if selection == 'C':
        date = input("Enter date that you'd like to mark complete: ")
        tracker.markDateComplete(date)
        config.push(tracker)
        displayDetails(tracker, config)
    elif selection == 'M':
        date = input("Enter date that you'd like to mark as missed: ")
        tracker.markDateMissed(date)
        config.push(tracker)
        displayDetails(tracker, config)
    
if __name__ == '__main__':
    welcome()
    config = ConfigManager('config.json')
    config.load()
    tracker = config.getTracker()
    whatNext(tracker, config) if tracker else firstRun(config)
