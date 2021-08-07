import unittest
from day import Day
from journal_entry import Entry

class TestDay(unittest.TestCase):
    def test_init(self):
        id = 1
        date = '2021-08-01'
        day = Day(id, date)
        self.assertEqual(day.id, id)
        self.assertEqual(day.iso_date, date)
        self.assertFalse(day.completed)
        self.assertIsInstance(day.log, Entry)
    
    def test_init_optional_params(self):
        id = 1
        date = '2021-08-01'
        content = "My journal entry goes here"
        entry = Entry(content)
        day = Day(id, date, True, entry)
        self.assertEqual(day.id, id)
        self.assertEqual(day.iso_date, date)
        self.assertTrue(day.completed)
        self.assertIsInstance(day.log, Entry)
        self.assertEqual(day.log.content,content)
    
    def test_init_journal_as_dict(self):
        id = 1
        date = '2021-08-01'
        entry = {
                "content": "I think I have the journal feature working!!!!!!!!! I'm about to lose my mind. Added some more text.",
                "date_created": "2021-07-27",
                "last_modified": "2021-07-27T01:21:57.898677"
            }
        day = Day(id, date, log=entry)
        self.assertFalse(day.completed)
        self.assertIsInstance(day.log, Entry)
        self.assertEqual(day.log.content, entry['content'])
    
    def test_update_entry(self):
        id = 1
        date = '2021-08-01'
        content = "My journal entry goes here"
        entry = Entry(content)
        day = Day(id, date, True, entry)
        new_content = "New journal content"
        day.modifyEntry(new_content)
        self.assertEqual(day.log.content,new_content)
    
    def test_load_cls_method(self):
        day_info = {
            "id": 84,
            "iso_date": "2021-07-26",
            "completed": True,
            "log": {
                "content": "I think I have the journal feature working!!!!!!!!! I'm about to lose my mind. Added some more text.",
                "date_created": "2021-07-27",
                "last_modified": "2021-07-27T01:21:57.898677"
            }
        }
        day = Day.load(day_info)
        self.assertIsInstance(day, Day)
        self.assertEqual(day.id, day_info['id'])
        self.assertEqual(day.iso_date, day_info['iso_date'])
        self.assertEqual(day.completed, day_info['completed'])
        self.assertIsInstance(day.log, Entry)
    
    def test_load_cls_method_bad_data(self):
        empty_day_info = {}
        day = Day.load(empty_day_info)
        self.assertIsNone(day)
        day_info_bad_key = {
            "iid": 84,
            "iso_date": "2021-07-26",
            "completed": True,
            "log": None
        }
        day = Day.load(day_info_bad_key)
        self.assertIsNone(day)
        day_info_xtra_key = {
            "id": 84,
            "iso_date": "2021-07-26",
            "completed": True,
            "log": None,
            "extra_key": True
        }
        day = Day.load(day_info_xtra_key)
        self.assertIsNone(day)
        day_info_not_dict = "String"
        day = Day.load(day_info_not_dict)
        self.assertIsNone(day)
        day_info_non_iso = {
            "id": 84,
            "iso_date": "07-26-2021",
            "completed": True,
            "log": None,
            "extra_key": True
        }
        day = Day.load(day_info_non_iso)
        self.assertIsNone(day)
    