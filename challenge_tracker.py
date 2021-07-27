import json
import datetime as dt
from day import *
from journal_entry import Entry

# Should I add an attribute that keeps track of the challenge status? 
#   (Ex. Not Started, In Progress, Done)

class ChallengeTracker:
    def __init__(self, start_date: str, duration: int) -> None:
        self.start_date = dt.date.fromisoformat(start_date)
        self.duration = duration
        self.end_date = self.getEndDate()
        #self.punchcard = self.createNewPunchcard()
        self.days = self.createDays()

    def getEndDate(self) -> dt.date:
        return self.start_date + dt.timedelta(days=self.duration-1)
    
    def createNewPunchcard(self):
        punchcard = {}
        for key in range(1,self.duration+1):
            punchcard[key] = False
        return punchcard
    
    def createDays(self):
        return [Day(day, self.getDateFromDay(day)) for day in range(1, self.duration + 1)]

    def isActive(self) -> bool:
        return self.start_date <= dt.date.today() and self.end_date >= dt.date.today()

    def currentDay(self) -> int:
        if self.isActive():
            days_from_start_date = (dt.date.today() - self.start_date + dt.timedelta(days=1)).days
            return days_from_start_date if days_from_start_date > 0 else 0
        else:
            raise RuntimeError("currentDay cannot be called on an inactive tracker.")
    
    def remainingDays(self) -> int:
        if self.isActive():
            return self.duration - self.currentDay()
        else:
            raise RuntimeError("remainingDays cannot be called on an inactive tracker.")
    
    def getDayFromDate(self, date):
        return (dt.date.fromisoformat(date) - self.start_date + dt.timedelta(days=1)).days
    
    def getDateFromDay(self,d):
        return (self.start_date + dt.timedelta(days=d-1)).isoformat()

    def markDateComplete(self, date):
        id = self.getDayFromDate(date)
        selected_day = None

        for day in self.days:
            if day.id == id:
                selected_day = day
                break
            else:
                continue

        if selected_day and selected_day.id > 0 and selected_day.id <=self.duration:
            selected_day.completed = True

    def markDateMissed(self, date):
        id = self.getDayFromDate(date)
        selected_day = None

        for day in self.days:
            if day.id == id:
                selected_day = day
                break
            else:
                continue

        if selected_day and selected_day.id > 0 and selected_day.id <=self.duration:
            selected_day.completed = False
    
    def totalMissedDays(self) -> int:
        values = [day.completed for day in self.days if day.id < self.currentDay()]   
        return values.count(False)
    
    def completedDays(self) -> int:
        return self.currentDay() - self.totalMissedDays()
    
    def createJournalEntry(self, date, content=None) -> None:
        id = self.getDayFromDate(date)
        selected_day = None

        for day in self.days:
            if day.id == id:
                selected_day = day
                break
            else:
                continue

        selected_day.journal_entry = Entry(content)
    
    def getJournalEntry(self, date) -> str:
        id = self.getDayFromDate(date)
        selected_day = None

        for day in self.days:
            if day.id == id:
                selected_day = day
                break
            else:
                continue
        
        # Return journal entry content if exsits.
        # Create new journal entry if doesn't exist.
        if selected_day.journal_entry:
            return selected_day.journal_entry.content
        else:
            selected_day.journal_entry = Entry()

    def modifyJournalEntry(self, date: str, content: str) -> None:
        id = self.getDayFromDate(date)
        selected_day = None

        for day in self.days:
            if day.id == id:
                selected_day = day
                break
            else:
                continue

        selected_day.journal_entry.modify(content)

    def asJSONObj(self) -> dict:
        tracker_object = {
            'start_date': self.start_date.isoformat(),
            'duration': self.duration,
            'end_date': self.end_date.isoformat(),
            'days': [d.asJSONObj() for d in self.days]
        }
        return tracker_object

tracker = ChallengeTracker("2021-05-04", 100)
with open("jope.json", "w") as write_file:
    json.dump(tracker.asJSONObj(), write_file, indent=4)