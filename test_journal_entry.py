import unittest
import datetime as dt
import challenge_tracker as trckr
from journal_entry import Entry

class TestJournalEntry(unittest.TestCase):
    def test_init_no_arguments(self):
        today = dt.datetime.now().isoformat()
        new_entry = Entry()
        print(f"DC: {new_entry.date_created}\nLM:{new_entry.last_modified}")
        # self.assertEqual(new_entry.date_created, today)
        # self.assertEqual(new_entry.last_modified, today)
        self.assertEqual(new_entry.content, "Today's Progress: \nThoughts: ")
    
    def test_init_with_arguments(self):
        date_created = "2021-07-01"
        last_modified = "2021-07-07"
        content = "A journal entry"
        entry = Entry(content,date_created,last_modified)
        self.assertEqual(entry.content, content)
        self.assertEqual(entry.date_created, date_created)
        self.assertEqual(entry.last_modified, last_modified)

    def test_modify(self): 
        creation_date = "2021-07-05"
        entry = Entry(date_created=creation_date)
        new_content = "Some random text."
        entry.modify(new_content)
        self.assertEqual(entry.content, new_content)
        last_modified = dt.datetime.fromisoformat(entry.last_modified)
        self.assertGreater(last_modified, dt.datetime.fromisoformat(creation_date))

    def test_asJSONObj(self):
        entry = Entry("My content goes here")
        entry.modify("My content goes here with new stuff")
        json_entry = entry.asJSONObj()
        self.assertEqual(entry.date_created, json_entry['date_created'])
        self.assertEqual(entry.last_modified, json_entry['last_modified'])
        self.assertEqual(entry.content, json_entry['content'])
        j_keys = list(json_entry.keys())
        j_keys.sort()
        self.assertEqual(j_keys,['content', 'date_created', 'last_modified'])
    
    def test_load(self):
        imported_entry = {
                "content": "I think I have the journal feature working!!!!!!!!! I'm about to lose my mind. Added some more text.",
                "date_created": "2021-07-27",
                "last_modified": "2021-07-28T01:21:57.898677"
            }
        entry = Entry.load(imported_entry)
        content = imported_entry['content']
        date_created = imported_entry['date_created']
        last_modified = imported_entry['last_modified']
        self.assertEqual(entry.content,content)
        self.assertEqual(entry.date_created, date_created)
        self.assertEqual(entry.last_modified, last_modified)
    
    def test_load_bad_data(self):
        bad_data = 9
        entry = Entry.load(bad_data)
        self.assertIsNone(entry)

TestJournalEntry().test_init_no_arguments()