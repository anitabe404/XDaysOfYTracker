import datetime as dt

# Should I add an attribute that keeps track of the challenge status? 
#   (Ex. Not Started, In Progress, Done)

class ChallengeTracker:
    def __init__(self, start_date: str, duration: int) -> None:
        self.start_date = dt.date.fromisoformat(start_date)
        self.duration = duration
        self.end_date = self.getEndDate()

    def getEndDate(self) -> dt.date:
        return self.start_date + dt.timedelta(days=self.duration-1)
    
    def currentDay(self) -> int:
        days_from_start = (dt.date.today() - self.start_date + dt.timedelta(days=1)).days
        
        if days_from_start < 0:
            return 0
        elif days_from_start > self.duration:
            return 'DONE'
        else:
            return days_from_start