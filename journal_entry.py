import datetime as dt

class Entry:
    def __init__(self, content=None):
        self.date_created = dt.date.today().isoformat()
        self.last_modified = dt.date.today().isoformat() # Should this be a datetime object?
        self.content = content or "Today's Progress: \nThoughts: \nLink to work: "

    def modify(self, new_content: str) -> None:
        self.content = new_content
        self.last_modified = dt.datetime.now().isoformat()
    
    def asJSONObj(self):
        return {
                    'content': self.content,
                    'date_created': self.date_created,
                    'last_modified': self.last_modified
        }