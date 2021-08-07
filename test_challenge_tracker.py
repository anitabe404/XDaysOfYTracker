import unittest
import datetime as dt
from challenge_tracker import ChallengeTracker
import day

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
    
    def test_getDayFromDate(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        today = dt.date.today().isoformat()
        self.assertEqual(tracker.getDayIdFromDate(today), delta + 1)
    
    def test_getDateFromDay(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        today = dt.date.today().isoformat()
        self.assertEqual(tracker.getDateFromDayId(delta+1),today)
    
    def test_getDayFromDays(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 20
        tracker = ChallengeTracker(date, duration)
        selected_day = tracker.selectDayFromDays(delta+1)
        self.assertEqual(selected_day.id, delta+1)
        self.assertEqual(selected_day.iso_date, dt.date.today().isoformat())

    def test_markDateComplete(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        completed_date = dt.date.today().isoformat()
        id = tracker.getDayIdFromDate(completed_date)
        tracker.markDateComplete(completed_date)
        selected_day = tracker.selectDayFromDays(id)
        self.assertTrue(selected_day.completed)
    
    def test_markDateMissed(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        missed_day = dt.date.today().isoformat()
        missed_day_id = tracker.getDayIdFromDate(missed_day)
        tracker.markDateComplete(missed_day)
        self.assertTrue(tracker.selectDayFromDays(missed_day_id).completed)
        tracker.markDateMissed(missed_day)
        self.assertFalse(tracker.selectDayFromDays(missed_day_id).completed)
    
    def test_totalMissedDays(self):
        delta = 5
        date = (dt.date.today() - dt.timedelta(days=delta)).isoformat()
        duration = 100
        tracker = ChallengeTracker(date, duration)
        missed_day = dt.date.today().isoformat()
        tracker.markDateComplete(missed_day)
        self.assertEqual(tracker.totalMissedDays(), delta)
    
    def test_createDays(self):
        delta = 5
        start_date = dt.date.today() - dt.timedelta(days=delta)
        duration = 20
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        self.assertEqual(len(tracker.days), duration)
        for day in tracker.days:
            # Confirm id is in range of 1 to duration
            self.assertIn(day.id,range(1,duration+1))

            # Confirm day and date are aligned
            date_obj = dt.date.fromisoformat(day.iso_date)
            self.assertGreaterEqual(date_obj,start_date)
            self.assertLessEqual(date_obj, tracker.end_date)
            self.assertEqual(day.iso_date, tracker.getDateFromDayId(day.id))

            # Confirm completion status is set to false
            self.assertFalse(day.completed)

            # Confirm log exists
            self.assertTrue(day.log)
    
    def test_modifyLog(self):
        delta = 5
        today = dt.date.today()
        start_date = today - dt.timedelta(days=delta)
        duration = 20
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        new_content = "Modified content"
        tracker.modifyLog(start_date.isoformat(), new_content)
        expected_output = f"Day {tracker.getDayIdFromDate(tracker.start_date.isoformat())}: {tracker.start_date.strftime('%b %d, %Y')}\n{new_content}"
        self.assertEqual(tracker.viewLog(start_date.isoformat()), expected_output)    
    
    def test_asJSONObj(self):
        delta = 5
        start_date = dt.date.today() - dt.timedelta(days=delta)
        duration = 20
        tracker = ChallengeTracker(start_date.isoformat(), duration)
        json_data = tracker.asJSONObj()
        self.assertEqual(tracker.start_date.isoformat(), json_data['start_date'])
        self.assertEqual(json_data['duration'], duration)
        self.assertEqual(json_data['end_date'], tracker.end_date.isoformat())
        self.assertEqual(len(json_data['days']), duration)

if __name__ == "__main__":
    unittest.main()