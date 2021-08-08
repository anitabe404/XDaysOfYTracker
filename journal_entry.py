import datetime as dt

class Entry:
    VALID_KEYS = ['content', 'date_created', 'last_modified']

    def __init__(self, content:str=None, date_created=None, last_modified=None):
        self.content = content or "Today's Progress: \nThoughts: "
        self.date_created = date_created or dt.datetime.today().isoformat()
        self.last_modified = last_modified or dt.datetime.today().isoformat()
        
    def modify(self, new_content: str) -> None:
        self.content = new_content
        self.last_modified = dt.datetime.now().isoformat()
    
    def asJSONObj(self):
        return {
                    'content': self.content,
                    'date_created': self.date_created,
                    'last_modified': self.last_modified
        }
    
    @classmethod
    def load(cls, imported_data:dict):
        if not isinstance(imported_data,dict):
            return None
            
        # content_fail_flag = False
        iso_fail_flag = False
        last_mod_fail_flag = False
        invalid_key_fail_flag = False

        # Check that keys are valid.
        imported_keys = list(imported_data.keys())
        imported_keys.sort()
        if imported_keys != Entry.VALID_KEYS:
            invalid_key_fail_flag = True
            print(f"Entry - Invalid key: {invalid_key_fail_flag}.")
            return None

        content = imported_data['content']
        date_created = imported_data['date_created']
        last_modified = imported_data['last_modified']
        try:
            dc = dt.datetime.fromisoformat(date_created)
            lm = dt.datetime.fromisoformat(last_modified)
            last_mod_fail_flag = lm < dc
        except:
            iso_fail_flag = True
            print("Dates are not in iso format.")
        
        return Entry(content, date_created, last_modified) \
                if not (iso_fail_flag or last_mod_fail_flag) else None          
