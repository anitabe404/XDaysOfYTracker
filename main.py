import datetime as dt
from challenge_tracker import *
from config_manager import *

def welcome():
    print("===================================================================")
    print("Welcome to the XDaysofY Challenge Tracker")
    print("===================================================================")

def firstRun():
    start_date = input('Enter start date in ISO format: ')
    duration = int(input('Enter challenge duration in days: '))
    tracker = ChallengeTracker(start_date, duration)
    # export tracker to config file
    displayDetails(tracker)

def displayDetails(tracker):
    print("")
    print("================== Your Challenge Information ====================")
    print(f'Your start date is {tracker.start_date.strftime("%b %d, %Y")}')
    print(f'Your end date is {tracker.end_date.strftime("%b %d, %Y")}')
    print(f'You are currently on Day {tracker.currentDay()}')
    print(f'You have {tracker.remainingDays()} days left')
    print(f'You have missed a total of {tracker.missedDays()} days')
    print("===================================================================")
    print("")
    whatNext(tracker)

def whatNext(tracker):
    print("-----------------------------------------------------------")
    print("What would you like to do?")
    print("(D)isplay challenge details")
    print("(S)et a day to complete or missed")
    selection = input("> ").upper()
    print("-----------------------------------------------------------")

    if selection == "D":
        displayDetails(tracker)
    elif selection == "S":
        setDay(tracker)
    else:
        whatNext(tracker)

def setDay(tracker):
    print("Do you want to:")
    print("(C)omplete a day")
    print("(M)ark a day as missed")
    selection = input("> ").upper()

    if selection == 'C':
        date = input("Enter date that you'd like to mark complete: ")
        tracker.markDateComplete(date)
        # Update config file
        displayDetails(tracker)
    elif selection == 'M':
        date = input("Enter date that you'd like to mark as missed: ")
        tracker.markDateMissed(date)
        # Update config file
        displayDetails(tracker)
    
if __name__ == '__main__':
    welcome()
    config = ConfigManager('anita.json')
    config.load()
    tracker = config.getTracker()
    whatNext(tracker) if tracker else firstRun()
