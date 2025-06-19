# src/data_seed.py

from datetime import datetime, timedelta
from habit import Habit
from tracker import HabitTracker
from storage import save_data

def generate_checkoffs(start_date, count, step_days):
    """
    Generate a list of check-off dates as strings, starting from 'start_date',
    spaced by 'step_days', repeated 'count' times.
    """
    return [(start_date + timedelta(days=i * step_days)).strftime('%Y-%m-%d') for i in range(count)]

def seed_data():
    tracker = HabitTracker()

    today = datetime.today()

    # 1. Daily habit (4 weeks = 28 days)
    habit1 = Habit("Morning Jog", "DAILY")
    habit1.checkoff_dates = generate_checkoffs(today - timedelta(days=27), 28, 1)

    # 2. Weekly habit (4 weeks = 4 checkoffs)
    habit2 = Habit("Grocery Shopping", "WEEKLY")
    habit2.checkoff_dates = generate_checkoffs(today - timedelta(weeks=3), 4, 7)

    # 3. Monthly habit (4 months = 4 checkoffs)
    habit3 = Habit("Budget Review", "MONTHLY")
    habit3.checkoff_dates = [
        (today.replace(day=1) - timedelta(days=90)).strftime('%Y-%m-%d'),  # 3 months ago
        (today.replace(day=1) - timedelta(days=60)).strftime('%Y-%m-%d'),  # 2 months ago
        (today.replace(day=1) - timedelta(days=30)).strftime('%Y-%m-%d'),  # 1 month ago
        today.replace(day=1).strftime('%Y-%m-%d')                          # current month
    ]

    # Add habits to tracker
    tracker.add_habit(habit1)
    tracker.add_habit(habit2)
    tracker.add_habit(habit3)

    # Save to persistent file
    save_data(tracker)
    print("✅ Habit data seeded and saved successfully.")

if __name__ == "__main__":
    seed_data()
