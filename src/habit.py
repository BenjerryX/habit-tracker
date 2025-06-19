# src/habit.py
from enum import Enum
from datetime import datetime, timedelta

class Periodicity(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        # Ensure that 'periodicity' is passed as a string (DAILY, WEEKLY, MONTHLY)
        self.periodicity = Periodicity[periodicity.upper()]  # Convert the string to Enum
        self.checkoff_dates = []  # List to store check-off dates
        self.current_streak = 0  # Legacy field (not used anymore in streak())

    def add_checkoff(self):
        """
        Mark this habit as completed for today by adding the current date.
        """
        today = datetime.today().strftime('%Y-%m-%d')

        # Avoid duplicate check-offs for the same day
        if today not in self.checkoff_dates:
            self.checkoff_dates.append(today)
            self.current_streak += 1  # Maintain backward compatibility (not used in streak logic)

    def calculate_streak(self):
        """
        Calculate the streak based on the habit's periodicity and check-off dates.
        Respects DAILY, WEEKLY, and MONTHLY rules.
        """
        if not self.checkoff_dates:
            return 0

        # Sort check-off dates from oldest to newest
        dates = sorted(datetime.strptime(date, '%Y-%m-%d') for date in self.checkoff_dates)
        streak = 1  # Start with 1 for most recent entry

        for i in range(len(dates) - 1, 0, -1):
            delta = dates[i] - dates[i - 1]

            if self.periodicity == Periodicity.DAILY and delta.days == 1:
                streak += 1
            elif self.periodicity == Periodicity.WEEKLY and 1 <= delta.days <= 7:
                streak += 1
            elif self.periodicity == Periodicity.MONTHLY and dates[i].month != dates[i - 1].month:
                streak += 1
            else:
                break  # Break streak if the periodicity pattern is not maintained

        return streak

    def streak(self):
        """
        Return the dynamically calculated streak value.
        """
        return self.calculate_streak()

