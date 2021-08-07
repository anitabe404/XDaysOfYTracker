import json
import datetime as dt
from day import *
from journal_entry import Entry

class ChallengeTracker:
    def __init__(self, iso_start_date: str, duration: int) -> None:
        self.start_date = dt.date.fromisoformat(iso_start_date)
        self.duration = duration
        self.end_date = self.start_date + dt.timedelta(days=self.duration-1)
        self.days = [Day(id, self.getDateFromDayId(id)) for id in range(1, self.duration + 1)]
    
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
    
    def getDayIdFromDate(self, date):
        return (dt.date.fromisoformat(date) - self.start_date + dt.timedelta(days=1)).days
    
    def getDateFromDayId(self, id):
        return (self.start_date + dt.timedelta(days=id-1)).isoformat()

    def selectDayFromDays(self, id):
        selected_day = None
        for day in self.days:
            if day.id == id:
                selected_day = day
                break  
        return selected_day

    def markDateComplete(self, date):
        id = self.getDayIdFromDate(date)
        selected_day = self.selectDayFromDays(id)

        if selected_day and selected_day.id > 0 and selected_day.id <=self.duration:
            selected_day.completed = True

    def markDateMissed(self, date):
        id = self.getDayIdFromDate(date)
        selected_day = self.selectDayFromDays(id)

        if selected_day and selected_day.id > 0 and selected_day.id <=self.duration:
            selected_day.completed = False
    
    def totalMissedDays(self) -> int:
        values = [day.completed for day in self.days if day.id < self.currentDay()]   
        return values.count(False)
    
    def totalCompletedDays(self) -> int:
        return self.currentDay() - self.totalMissedDays()
    
    def viewLog(self, date) -> str:
        id = self.getDayIdFromDate(date)
        selected_day = self.selectDayFromDays(id)
        if selected_day:
            return selected_day.viewLog()

    def modifyLog(self, date: str, content: str) -> None:
        id = self.getDayIdFromDate(date)
        selected_day = self.selectDayFromDays(id)
        if selected_day:
            selected_day.modifyLog(content)

    def asJSONObj(self) -> dict:
        serializabble_tracker = {
            'start_date': self.start_date.isoformat(),
            'duration': self.duration,
            'end_date': self.end_date.isoformat(),
            'days': [d.asJSONObj() for d in self.days]
        }
        return serializabble_tracker