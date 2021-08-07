import json
from journal_entry import Entry
import datetime as dt

class Day():
    VALID_KEYS = ['completed', 'id', 'iso_date', 'log']
    def __init__(self, day_id: int, iso_date: str, completed:bool=False, log=None) -> None:
        self.id = day_id
        self.iso_date = iso_date
        self.completed = completed
        if isinstance(log, Entry):
            self.log = log
        elif isinstance(log, dict):
            self.log = Entry.load(log) or Entry() # if load fails, create new Entry
        else:
            self.log = Entry()
    
    def viewLog(self):
        mon_dd_yyyy = dt.date.fromisoformat(self.iso_date).strftime("%b %d, %Y")
        return f"Day {self.id}: {mon_dd_yyyy}\n{self.log.content}"

    def modifyLog(self, new_content):
        self.log.modify(new_content)

    def asJSONObj(self) -> dict:
        if isinstance(self.log, Entry):
            return {
                     "id": self.id, 
                    "iso_date": self.iso_date,
                    "completed": self.completed, 
                    "log": self.log.asJSONObj()   
            }
        else:
            return {
                        "id": self.id, 
                        "iso_date": self.iso_date,
                        "completed": self.completed, 
                        "log": self.log
                    }
    
    @classmethod
    def load(cls, imported_data:dict):
        if not isinstance(imported_data, dict):
            return None

        # fail flags
        id_fail_flag = False
        iso_fail_flag = False
        completed_fail_flag = False

        imported_keys = list(imported_data.keys())
        imported_keys.sort()
        if imported_keys == Day.VALID_KEYS:
            id = imported_data['id']
            if not isinstance(id, int):
                id_fail_flag = True

            iso_date = imported_data['iso_date']
            try:
                dt.date.fromisoformat(iso_date)
            except:
                iso_fail_flag = True

            completed = imported_data['completed']
            if not isinstance(completed, bool):
                completed_fail_flag = True
            
            log = Entry.load(imported_data['log'])

            if not (id_fail_flag or iso_fail_flag or completed_fail_flag):
                return cls(id, iso_date, completed, log)
        
        return None
