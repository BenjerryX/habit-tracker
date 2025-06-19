# src/cli.py

from habit import Habit, Periodicity
from tracker import HabitTracker
from analytics import Analytics
from storage import save_data, load_data

def main():
    tracker = load_data()  # Load existing tracker or create a new one
    analytics = Analytics(tracker)

    while True:
        print("\n1. Add habit")
        print("2. List all habits")
        print("3. Check off habit")
        print("4. View habit analytics")
        print("5. Save and exit")

        choice = input("Enter choice: ")

        if choice == '1':
            # Add habit
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (DAILY, WEEKLY, MONTHLY): ").upper()

            try:
                habit = Habit(name, periodicity)
                tracker.add_habit(habit)
                print(f"Habit '{name}' added.")
            except KeyError:
                print("Invalid periodicity. Please enter DAILY, WEEKLY, or MONTHLY.")

        elif choice == '2':
            # List habits
            print("\nList of habits:")
            for habit in tracker.habits:
                print(f"Name: {habit.name}, Periodicity: {habit.periodicity.name}, Current Streak: {habit.streak()}")

        elif choice == '3':
            # Check off habit
            habit_name = input("Enter the name of the habit to check off: ")
            tracker.check_off_habit(habit_name)

        elif choice == '4':
            # View habit analytics
            print("\nHabit Analytics:")
            print(f"Total habits: {analytics.total_habits()}")
            print(f"Total checked off habits: {analytics.total_checked_off()}")
            print(f"Highest streak value: {analytics.highest_streak_value()}")
            print(f"Lowest non-zero streak value: {analytics.lowest_streak_value()}")
            longest = analytics.longest_streak()
            if longest:
                print(f"Habit with longest streak: {longest.name} ({longest.streak()})")
            else:
                print("No streaks available yet.")

        elif choice == '5':
            # Save and exit
            save_data(tracker)
            print("Progress saved. Exiting...")
            break

if __name__ == "__main__":
    main()
