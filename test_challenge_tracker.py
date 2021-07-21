import unittest
import datetime as dt
from challenge_tracker import ChallengeTracker
from punch_card import PunchCard

class TestChallengeTracker(unittest.TestCase):
    def test_start_date_is_date_obj(self):
        day_manager = ChallengeTracker("2021-05-04", 100)
        self.assertIsInstance(day_manager.start_date, dt.date)
    
    def test_duration_is_int(self):
        day_manager = ChallengeTracker("2021-05-04", 100)
        self.assertIsInstance(day_manager.duration, int)
    
    def test_end_date(self):
        day_manager = ChallengeTracker("2021-05-04", 100)
        self.assertEqual(day_manager.end_date, dt.date.fromisoformat('2021-08-11'))
    
    def test_current_day(self):
        today = dt.date.today()
        day_manager = ChallengeTracker(today.isoformat(), 100)
        self.assertEqual(day_manager.currentDay(), 1)

    def test_current_day_for_future_start_date(self):
        future_start_date = (dt.date.today() + dt.timedelta(days=1)).isoformat()
        tracker = ChallengeTracker(future_start_date, 100)
        with self.assertRaises(RuntimeError):
            tracker.currentDay()
    
    def test_current_day_for_day_after_end(self):
        start_date = dt.date.today() - dt.timedelta(days=100)
        tracker = ChallengeTracker(start_date.isoformat(), 50)
        with self.assertRaises(RuntimeError):
            tracker.currentDay()

    def test_remaining_days(self):
        tracker = ChallengeTracker(dt.date.today().isoformat(), 5)
        self.assertEqual(tracker.remainingDays(), 4)
    
    def test_remaining_days_after_challenge_end(self):
        start_date = dt.date.today() - dt.timedelta(days=101)
        tracker = ChallengeTracker(start_date.isoformat(), 100)
        with self.assertRaises(RuntimeError):
            tracker.remainingDays()

    def test_challenge_is_active(self):
        start_date = dt.date.today() - dt.timedelta(days=1)
        duration = 100
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        self.assertEqual(tracker.isActive(), True)

    def test_challenge_is_active_for_future_start(self):
        start_date = dt.date.today() + dt.timedelta(days=1)
        duration = 100
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        self.assertEqual(tracker.isActive(), False)
    
    def test_challenge_is_active_for_finished_challenge(self):
        start_date = dt.date.today() - dt.timedelta(days=101)
        duration = 100
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        self.assertEqual(tracker.isActive(), False)

    def test_createPunchcard(self):
        today = dt.date.today().isoformat()
        duration = 5
        tracker = ChallengeTracker(today, duration)
        my_card = tracker.punchcard
        num_of_false = list(my_card.values()).count(False)
        num_of_true = list(my_card.values()).count(True)
        self.assertEqual(num_of_false, duration)
        self.assertEqual(num_of_true, 0)

    def test_punchcard(self):
        tracker = ChallengeTracker('2021-05-04', 100)
        punchcard = tracker.punchcard
        self.assertIsInstance(punchcard, dict)
        self.assertEqual(len(punchcard),100)
        punchcard_keys = list(punchcard.keys())
        punchcard_keys.sort()
        self.assertEqual(punchcard_keys, list(range(1,101)))
    
    def test_getDayFromDate(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        today = dt.date.today().isoformat()
        self.assertEqual(tracker.getDayFromDate(today), delta + 1)
    
    def test_markDateComplete(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        completed_date = dt.date.today().isoformat()
        tracker.markDateComplete(completed_date)
        self.assertEqual(tracker.punchcard[delta+1], True)
    
    def test_markDateMissed(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        missed_day = dt.date.today().isoformat()
        tracker.markDateComplete(missed_day)
        self.assertEqual(tracker.punchcard[delta+1], True)
        tracker.markDateMissed(missed_day)
        self.assertEqual(tracker.punchcard[delta+1], False)
    
    def test_missedDays(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        missed_day = dt.date.today().isoformat()
        tracker.markDateComplete(missed_day)
        self.assertEqual(tracker.missedDays(), delta)


if __name__ == "__main__":
    unittest.main()