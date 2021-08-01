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
        self.assertIsNone(day.journal_entry)
    
    def test_init_optional_params(self):
        id = 1
        date = '2021-08-01'
        content = "My journal entry goes here"
        entry = Entry(content)
        day = Day(id, date, True, entry)
        self.assertEqual(day.id, id)
        self.assertEqual(day.iso_date, date)
        self.assertTrue(day.completed)
        self.assertIsInstance(day.journal_entry, Entry)
        self.assertEqual(day.journal_entry.content,content)
    
    def test_init_journal_as_dict(self):
        id = 1
        date = '2021-08-01'
        entry = {
                "content": "I think I have the journal feature working!!!!!!!!! I'm about to lose my mind. Added some more text.",
                "date_created": "2021-07-27",
                "last_modified": "2021-07-27T01:21:57.898677"
            }
        day = Day(id, date, journal_entry=entry)
        self.assertFalse(day.completed)
        self.assertIsInstance(day.journal_entry, Entry)
        self.assertEqual(day.journal_entry.content, entry['content'])
    
    # def test_init_invalid_arg_for_journal(self):
    #     id = 1
    #     date = '2021-08-01'
    #     entry = "A string and not an Entry object"
    
    def test_load_cls_method(self):
        day_info = {
            "id": 84,
            "iso_date": "2021-07-26",
            "completed": True,
            "journal_entry": {
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
        self.assertIsInstance(day.journal_entry, Entry)
        