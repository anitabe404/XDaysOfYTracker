import datetime as dt

# Should I add an attribute that keeps track of the challenge status? 
#   (Ex. Not Started, In Progress, Done)

class ChallengeTracker:
    def __init__(self, start_date: str, duration: int) -> None:
        self.start_date = dt.date.fromisoformat(start_date)
        self.duration = duration
        self.end_date = self.getEndDate()
        self.punchcard = self.createNewPunchcard()

    def getEndDate(self) -> dt.date:
        return self.start_date + dt.timedelta(days=self.duration-1)
    
    def createNewPunchcard(self):
        punchcard = {}
        for key in range(1,self.duration+1):
            punchcard[key] = False
        return punchcard
    
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

    def markDateComplete(self, date):
        day = self.getDayFromDate(date)
        if day > 0 and day <= self.duration:
            self.punchcard[day] = True

    def markDateMissed(self, date):
        day = self.getDayFromDate(date)
        if day > 0 and day <=self.duration:
            self.punchcard[day] = False
    
    def totalMissedDays(self) -> int:
        values = [self.punchcard[key] for key in range(1, self.currentDay()+1)]   
        return values.count(False)
    
    def completedDays(self) -> int:
        return self.currentDay() - self.totalMissedDays()