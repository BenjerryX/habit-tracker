# src/tests/test_suite.py

import unittest
from datetime import datetime, timedelta
from habit import Habit
from tracker import HabitTracker
from analytics import Analytics

class TestHabitCreation(unittest.TestCase):
    def test_create_daily_habit(self):
        habit = Habit("Read Book", "DAILY")
        self.assertEqual(habit.name, "Read Book")
        self.assertEqual(habit.periodicity.name, "DAILY")
        self.assertEqual(habit.streak(), 0)

    def test_add_habit_to_tracker(self):
        tracker = HabitTracker()
        habit = Habit("Workout", "DAILY")
        tracker.add_habit(habit)
        self.assertIn(habit, tracker.habits)

class TestHabitEditing(unittest.TestCase):
    def test_checkoff_addition(self):
        habit = Habit("Meditate", "DAILY")
        habit.add_checkoff()
        self.assertEqual(len(habit.checkoff_dates), 1)

    def test_duplicate_checkoff(self):
        habit = Habit("Stretch", "DAILY")
        habit.add_checkoff()
        habit.add_checkoff()  # Should not add duplicate for same day
        self.assertEqual(len(habit.checkoff_dates), 1)

class TestHabitDeletion(unittest.TestCase):
    def test_remove_habit(self):
        tracker = HabitTracker()
        habit = Habit("Yoga", "DAILY")
        tracker.add_habit(habit)
        tracker.habits.remove(habit)
        self.assertNotIn(habit, tracker.habits)

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.tracker = HabitTracker()

        # Habit with 3 consecutive daily checkoffs
        self.daily = Habit("Journal", "DAILY")
        today = datetime.today()
        self.daily.checkoff_dates = [
            (today - timedelta(days=2)).strftime('%Y-%m-%d'),
            (today - timedelta(days=1)).strftime('%Y-%m-%d'),
            today.strftime('%Y-%m-%d')
        ]

        # Habit with no checkoffs
        self.empty = Habit("Call Mom", "WEEKLY")

        self.tracker.add_habit(self.daily)
        self.tracker.add_habit(self.empty)
        self.analytics = Analytics(self.tracker)

    def test_total_habits(self):
        self.assertEqual(self.analytics.total_habits(), 2)

    def test_total_checked_off(self):
        self.assertEqual(self.analytics.total_checked_off(), 1)

    def test_highest_streak_value(self):
        self.assertEqual(self.analytics.highest_streak_value(), 3)

    def test_lowest_streak_value(self):
        self.assertEqual(self.analytics.lowest_streak_value(), 3)

    def test_longest_streak_habit_name(self):
        self.assertEqual(self.analytics.longest_streak().name, "Journal")

if __name__ == '__main__':
    unittest.main()
