import json
import os.path
from challenge_tracker import *

class ConfigManager:
    VALID_TRACKER_KEYS = ['duration', 'end_date', 'punchcard', 'start_date']

    def __init__(self, file_name='config.json'):
        self.file_name = file_name
        self.tracker = None
    
    def loadJson(self):
        try:
            config_json = json.load(open(self.file_name))
        except:
            config_json = False
            print("Invalid Json")
        
        return config_json

    def trackerDict(self, config_json):
        try:
            imported_keys = list(config_json[0].keys())
            imported_keys.sort()
        except:
            imported_keys = None

        return config_json[0] if imported_keys == self.VALID_TRACKER_KEYS else False

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
            imported_card = data['punchcard']
            tracker = ChallengeTracker(start_date, duration)

            end_fail_flag = end_date != tracker.end_date.isoformat()

            punchcard = {}
            for k,v in imported_card.items():
                k = int(k)
                if k not in range(1,duration+1):
                    pc_keys_fail_flag = True
                    break
                else:
                    if isinstance(v, bool):
                        punchcard[k] = v
                    else:
                        pc_val_fail_flag = True
        else:
            data_fail_flag = True

        if not (data_fail_flag or end_fail_flag or pc_keys_fail_flag or pc_val_fail_flag):
            tracker.punchcard = punchcard
            self.tracker = tracker

        return None # function changes self.tracker to ChallengeTracker if data is valid


    def getTracker(self) -> ChallengeTracker:
        if self.tracker:
            return self.tracker
        else:
            return False

# file_name = './tests/good_tracker_data.json'
# config_man = ConfigManager(file_name)
# config_man.load()
# tracker = config_man.getTracker()
# print("the end")