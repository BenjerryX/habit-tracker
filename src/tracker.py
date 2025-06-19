# src/tracker.py

class HabitTracker:
    def __init__(self):
        self.habits = []  # List to store habits

    def add_habit(self, habit):
        """
        Add a new habit to the tracker.
        """
        self.habits.append(habit)

    def find_habit(self, habit_name):
        """
        Find and return a habit by its name.
        If not found, returns None.
        """
        return next((h for h in self.habits if h.name == habit_name), None)

    def check_off_habit(self, habit_name):
        """
        Mark a habit as checked off for today.
        """
        habit = self.find_habit(habit_name)
        
        if habit:
            habit.add_checkoff()  # Calls the add_checkoff method from the Habit class
            print(f"Checked off habit: {habit_name}")
        else:
            print(f"Habit with name '{habit_name}' not found.")
