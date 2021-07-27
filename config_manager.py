import day
import json
import os.path
from challenge_tracker import *
from journal_entry import Entry

class ConfigManager:
    VALID_TRACKER_KEYS = ['days', 'duration', 'end_date', 'start_date']

    def __init__(self, file_name='config.json'):
        self.file_name = file_name
        self.tracker = None
    
    def loadJson(self):
        try:
            config_json = json.load(open(self.file_name))
        except:
            config_json = False
            #print("Invalid Json")
        
        return config_json

    def trackerDict(self, config_json):
        try:
            imported_keys = list(config_json.keys())
            imported_keys.sort()
        except:
            imported_keys = None

        return config_json if imported_keys == self.VALID_TRACKER_KEYS else False

    def load(self):
        config_json = self.loadJson()
        data = self.trackerDict(config_json)
        data_fail_flag = False
        end_fail_flag = False
        pc_keys_fail_flag = False
        pc_val_fail_flag = False

        if data:
            start_date = data['start_date']
            duration = int(data['duration'])
            end_date = data['end_date']
            imported_days = data['days']
            days_list = None
            tracker = ChallengeTracker(start_date, duration)

            end_fail_flag = end_date != tracker.end_date.isoformat()

            # Create list of Day object
            days_list = [
                Day(
                    day['id'], 
                    day['iso_date'], 
                    day['completed'], 
                    day['journal_entry']
                ) for day in imported_days
            ]

            # punchcard = {}
            # for k,v in imported_card.items():
            #     k = int(k)
            #     if k not in range(1,duration+1):
            #         pc_keys_fail_flag = True
            #         break
            #     else:
            #         if isinstance(v, bool):
            #             punchcard[k] = v
            #         else:
            #             pc_val_fail_flag = True
        else:
            data_fail_flag = True

        if not (data_fail_flag or end_fail_flag): #or pc_keys_fail_flag or pc_val_fail_flag):
            # tracker.punchcard = punchcard
            tracker.days = days_list
            self.tracker = tracker

        return None # function changes self.tracker to ChallengeTracker if data is valid


    def getTracker(self) -> ChallengeTracker:
        if self.tracker:
            return self.tracker
        else:
            return False
    
    def push(self, tracker) -> None:
        # exportObj = [{}]
        # exportObj[0]['start_date'] = tracker.start_date.isoformat()
        # exportObj[0]['duration'] = tracker.duration
        # exportObj[0]['end_date'] = tracker.end_date.isoformat()
        # exportObj[0]['punchcard'] = tracker.punchcard
        # exportObj[0]['day'] = tracker.day.dayAsObject()
        jsonString = json.dumps(tracker.asJSONObj(), indent=4)
        jsonFile = open(self.file_name, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
# file_name = './tests/good_tracker_data.json'
# config_man = ConfigManager(file_name)
# config_man.load()
# tracker = config_man.getTracker()
# print("the end")