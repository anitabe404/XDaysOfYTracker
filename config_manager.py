import json
from challenge_tracker import *

class ConfigManager:
    def __init__(self, file_name='config.json'):
        self.file_name = file_name
    
    def loadJson(self):
        try:
            config_json = json.load(open(self.file_name))
        except:
            config_json = False
        
        return config_json

    def load(self):
        import_data = self.loadJson()
        return ChallengeTracker.load(import_data)

    def push(self, tracker) -> None:
        with open(self.file_name, "w") as fh:
            json.dump(tracker.asJSONObj(),fh, indent=4)