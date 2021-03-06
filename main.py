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
    print("(J)ournal: View Entry, Update Entry, or Export")
    selection = input("> ").upper()
    print("-----------------------------------------------------------")

    if selection == "D":
        displayDetails(tracker, config)
    elif selection == "S":
        setDay(tracker, config)
    elif selection == "J":
        editJournal(tracker,config)
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

def editJournal(tracker, config):
    print("Do you want to:")
    print("(V)iew an entry")
    print("(U)pdate an entry")
    print("(E)xport journal")
    selection = input("> ").upper()

    

    if selection == 'V':
        print("Enter ISO date of journal entry: ")
        date = input("> ")
        print("====================")
        print(tracker.viewLog(date))
        print("====================")
        input("(Press Enter to continue)")
        displayDetails(tracker, config)
    elif selection == "U":
        print("Enter ISO date of journal entry: ")
        date = input("> ")

        # Display current text
        print("Current Text:")
        print("====================")
        print(tracker.viewLog(date))
        print("====================")

        # Request new text
        print("")
        print("Enter new text.")
        new_content = input("> ")
        tracker.modifyLog(date, new_content)
        config.push(tracker)

        # Display new text
        print("")
        print("Here's your updated entry.")
        print("====================")
        print(tracker.viewLog(date))
        print("====================")
        input("Press Enter to continue")
        whatNext(tracker,config)
    elif selection == "E":
        tracker.exportLog()
        print("Log exported to log.txt")
        input("Press Enter to continue")
        whatNext(tracker,config)
    else:
        editJournal(tracker,config)
    
if __name__ == '__main__':
    welcome()
    config = ConfigManager('config.json')
    tracker = config.load()
    whatNext(tracker, config) if tracker else firstRun(config)
