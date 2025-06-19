# src/analytics.py 

class Analytics:
    def __init__(self, tracker):
        self.tracker = tracker

    def total_habits(self):
        """
        Return the total number of habits being tracked.
        """
        return len(self.tracker.habits)

    def total_checked_off(self):
        """
        Return the number of habits that have at least one check-off.
        """
        return sum(1 for habit in self.tracker.habits if habit.checkoff_dates)

    def longest_streak(self):
        """
        Return the habit with the highest current streak.
        If no habits have check-offs, returns None.
        """
        if not self.tracker.habits:
            return None

        # Use habit.streak() to get the dynamic streak value
        return max(self.tracker.habits, key=lambda habit: habit.streak(), default=None)

    def highest_streak_value(self):
        """
        Return the highest streak value among all habits.
        If no habits, return 0.
        """
        if not self.tracker.habits:
            return 0

        return max((habit.streak() for habit in self.tracker.habits), default=0)

    def lowest_streak_value(self):
        """
        Return the lowest non-zero streak value among all habits.
        If no habits have non-zero streaks, return 0.
        """
        non_zero_streaks = [habit.streak() for habit in self.tracker.habits if habit.streak() > 0]
        if not non_zero_streaks:
            return 0
        return min(non_zero_streaks)

    def habits_by_periodicity(self, periodicity):
        """
        Return a list of habits filtered by a given periodicity (e.g., DAILY, WEEKLY).
        """
        return [habit for habit in self.tracker.habits if habit.periodicity == periodicity]
