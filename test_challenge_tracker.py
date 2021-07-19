import unittest
import datetime as dt
from challenge_tracker import ChallengeTracker

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
        day_manager = ChallengeTracker(future_start_date, 100)
        self.assertEqual(day_manager.currentDay(),0)
    
    def test_current_day_for_day_after_end(self):
        start_date = dt.date.today() - dt.timedelta(days=100)
        day_manager = ChallengeTracker(start_date.isoformat(), 50)
        self.assertEqual(day_manager.currentDay(), "DONE")


if __name__ == "__main__":
    unittest.main()