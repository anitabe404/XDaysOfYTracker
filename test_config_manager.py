from challenge_tracker import ChallengeTracker
import unittest
import json
from config_manager import ConfigManager
import os.path

class TestConfigManager(unittest.TestCase):
    def test_init_with_file_name(self):
        file_name = 'test.json'
        config_man1 = ConfigManager(file_name)
        self.assertEqual(config_man1.file_name, file_name)
        
    def test_init_without_file_name(self):
        default_name = 'config.json'
        config_man2 = ConfigManager()
        self.assertEqual(config_man2.file_name, default_name)

    def test_loadJson_for_valid_json(self):
        file_name = './tests/valid.json'
        config_man = ConfigManager(file_name)
        self.assertTrue(config_man.loadJson())

    def test_loadJson_for_invalid_json(self):
        file_name = './tests/invalid.json'
        config_man = ConfigManager(file_name)
        self.assertFalse(config_man.loadJson())

    def test_loadJson_for_file_not_exists(self):
        file_name = 'doesnt_exist.json'
        config_man = ConfigManager(file_name)
        self.assertFalse(config_man.loadJson())
    
    # def test_isValidTracker(self):
    #     file_name = './tests/valid.json'
    #     config_man = ConfigManager(file_name)
    #     self.assertTrue(config_man.isValidTracker())
    
    def test_trackerDict(self):
        file_name = './tests/good_tracker_data.json'
        config_man = ConfigManager(file_name)
        valid_json_data = config_man.loadJson()
        tDict = config_man.trackerDict(valid_json_data)
        self.assertIsInstance(tDict, dict)
        self.assertTrue(tDict)
    
    # def test_trackerDict_bad_tracker_data(self):
    #     file_name = './tests/bad_tracker_data.json'
    #     config_man = ConfigManager(file_name)
    #     invalid_json_data = config_man.loadJson()
    #     self.assertFalse(config_man.trackerDict(invalid_json_data))

    def test_load(self):
        file_name = './tests/good_tracker_data.json'
        config_man = ConfigManager(file_name)
        config_man.load()
        self.assertTrue(config_man.getTracker())
    
    def test_load_for_invalid_tracker_data(self):
        file_name = './tests/bad_tracker_data.json'
        config_man = ConfigManager(file_name)
        config_man.load()
        self.assertFalse(config_man.getTracker())
    
    # def test_import_data_invalid_tracker_data(self):
    #     file_name = './tests/bad_tracker_data.json'
    #     config_man = ConfigManager(file_name)
    #     with self.assertRaises(RuntimeError):
    #         config_man.tracker()

    def test_push(self):
        comparison_file = "./tests/good_tracker_data_for_comparison.json"
        comparison_string = open(comparison_file).read()

        push_file = "./tests/good_tracker_data_from_push.json"
        config_for_push = ConfigManager(push_file)
        tracker_for_push = ChallengeTracker('2021-07-19', 5)
        tracker_for_push.markDateComplete('2021-07-19')
        tracker_for_push.markDateComplete('2021-07-20')
        config_for_push.push(tracker_for_push)
        push_string = open(push_file).read()
        
        self.assertEqual(push_string, comparison_string)
        