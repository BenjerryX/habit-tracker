# src/storage.py

import pickle
import os
from tracker import HabitTracker

DATA_FILE = "habit_data.pkl"

def save_data(tracker):
    """Save the tracker object to a file."""
    with open(DATA_FILE, "wb") as f:
        pickle.dump(tracker, f)

def load_data():
    """Load the tracker object from a file, or create a new one if loading fails."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "rb") as f:
                tracker = pickle.load(f)
                return tracker
        except (pickle.UnpicklingError, AttributeError, EOFError, ImportError, IndexError, ValueError) as e:
            print("\n⚠️  Warning: Failed to load existing data (probably outdated or broken).")
            print(f"Error details: {e}")
            print("Starting with a fresh Habit Tracker.\n")
            return HabitTracker()
    else:
        return HabitTracker()
