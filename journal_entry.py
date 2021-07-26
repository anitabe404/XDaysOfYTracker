import datetime as dt

class Entry:
    def __init__(self, day, date):
        self.day = day
        self.date = date
        self.date_created = dt.date.today().isoformat()
        self.last_modified = dt.date.today().isoformat() # Should this be a datetime object?
        self.content = "Today's Progress: \nThoughts: \nLink to work: "

    def modify(self, new_content: str) -> None:
        self.content = new_content
        self.last_modified = dt.datetime.now().isoformat()