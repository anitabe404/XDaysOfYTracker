import unittest
from punch_card import PunchCard

class TestPunchCard(unittest.TestCase):
    def test_init(self):
        size = 5
        my_card = PunchCard(size)
        self.assertIsInstance(my_card.slots, dict)
        self.assertEqual(len(my_card.slots), size)
        num_of_false = list(my_card.slots.values()).count(False)
        self.assertEqual(num_of_false, 5)
    
    def test_punch(self):
        size = 5
        my_card = PunchCard(size)
        punch_day = 3
        my_card.punch(punch_day)
        num_of_false = list(my_card.slots.values()).count(False)
        num_of_true = list(my_card.slots.values()).count(True)
        self.assertEqual(my_card.slots[punch_day], True)
        self.assertEqual(num_of_true, 1)
        self.assertEqual(num_of_false, size - 1)
    
    def test_punch_multi_punches(self):
        size = 5
        my_card = PunchCard(size)
        punch_days = [1,2,3]
        for day in punch_days:
            my_card.punch(day)

        for day in punch_days:
            self.assertEqual(my_card.slots[day], True)

        num_of_false = list(my_card.slots.values()).count(False)
        num_of_true = list(my_card.slots.values()).count(True)
        self.assertEqual(num_of_true, len(punch_days))
        self.assertEqual(num_of_false, size - len(punch_days))

    def test_unpunch(self):
        size = 5
        my_card = PunchCard(size)
        punch_day = 3
        my_card.punch(punch_day)
        my_card.unpunch(punch_day)
        num_of_false = list(my_card.slots.values()).count(False)
        num_of_true = list(my_card.slots.values()).count(True)
        self.assertEqual(my_card.slots[punch_day], False)
        self.assertEqual(num_of_true, 0)
        self.assertEqual(num_of_false, size)
    
    def test_unpunch_multi_punches(self):
        size = 5
        my_card = PunchCard(size)
        punch_days = [1,2,3]
        for day in punch_days:
            my_card.punch(day)

        my_card.unpunch(punch_days[1])
        self.assertEqual(my_card.slots[punch_days[0]], True)
        self.assertEqual(my_card.slots[punch_days[1]], False)
        self.assertEqual(my_card.slots[punch_days[2]], True)

        num_of_false = list(my_card.slots.values()).count(False)
        num_of_true = list(my_card.slots.values()).count(True)
        self.assertEqual(num_of_true, len(punch_days)-1)
        self.assertEqual(num_of_false, size - (len(punch_days) - 1))


