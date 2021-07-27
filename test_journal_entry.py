import unittest
import datetime as dt
import challenge_tracker as trckr
import journal_entry as je

class TestJournalEntry(unittest.TestCase):
    def test_init(self):
        today = dt.date.today()
        start_date = (today - dt.timedelta(days=4)).isoformat()
        duration = 10
        tracker = trckr.ChallengeTracker(start_date, duration)
        day = tracker.getDayFromDate(today.isoformat())
        new_entry = je.Entry(day, today.isoformat())
        self.assertEqual(new_entry.date_created, today.isoformat())
        self.assertEqual(new_entry.last_modified, today.isoformat())
        self.assertEqual(new_entry.content, "Today's Progress: \nThoughts: \nLink to work: ")

    def test_modify(self):
        today = dt.date.today()
        start_date = (today - dt.timedelta(days=4)).isoformat()
        duration = 10
        tracker = trckr.ChallengeTracker(start_date, duration)
        day = tracker.getDayFromDate(today.isoformat())
        new_entry = je.Entry(day, today.isoformat())
        new_content = "Some random text."
        new_entry.modify(new_content)
        self.assertEqual(new_entry.content, new_content)
        last_modified = dt.datetime.fromisoformat(new_entry.last_modified)
        date_created = dt.datetime.fromisoformat(new_entry.date_created)
        self.assertGreater(last_modified, date_created)

    def test_asJSONObj(self):
        today = dt.date.today()
        start_date = (today - dt.timedelta(days=4)).isoformat()
        duration = 10
        tracker = trckr.ChallengeTracker(start_date, duration)
        day = tracker.getDayFromDate(today.isoformat())
        journal_entry = je.Entry(day, today.isoformat())
        journal_dict = journal_entry.asJSONObj()
        self.assertEqual(journal_entry.date_created, journal_dict['date_created'])
        self.assertEqual(journal_entry.last_modified, journal_dict['last_modified'])
        self.assertEqual(journal_entry.content, journal_dict['content'])
        j_keys = list(journal_dict.keys())
        j_keys.sort()
        self.assertEqual(j_keys,['content', 'date_created', 'last_modified'])