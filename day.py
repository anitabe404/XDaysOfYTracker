import json
import journal_entry as je

class Day():
    def __init__(self, day: int, date: str, completed:bool=False, journal_entry=None) -> None:
        self.id = day
        self.iso_date = date
        self.completed = completed
        if isinstance(journal_entry, dict):
            self.journal_entry = je.Entry(journal_entry['content'])
            self.journal_entry.date_created = journal_entry['date_created']
            self.journal_entry.last_modified = journal_entry['last_modified']
        else:
            self.journal_entry = journal_entry

    def asJSONObj(self) -> dict:
        if isinstance(self.journal_entry, je.Entry):
            return {
                     "id": self.id, 
                    "iso_date": self.iso_date,
                    "completed": self.completed, 
                    "journal_entry": self.journal_entry.asJSONObj()   
            }
        else:
            return {
                        "id": self.id, 
                        "iso_date": self.iso_date,
                        "completed": self.completed, 
                        "journal_entry": self.journal_entry
                    }