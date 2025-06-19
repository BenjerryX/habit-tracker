# Habit Tracker Application

## Overview
This Habit Tracker is a Python-based CLI application designed to help users create, track, and analyze their habits with support for different periodicities: daily, weekly, and monthly. The app calculates habit streaks based on these periodicities, offering insights into consistency and progress.

## Features
- Add habits with specified periodicities (DAILY, WEEKLY, MONTHLY)
- Check off habits on their respective days
- View habit analytics such as total habits, checked-off habits, and streak statistics
- Persistent data storage with automatic saving/loading
- Modular codebase designed for maintainability and extensibility
- Comprehensive unit tests to ensure reliability

## Project Structure
- `src/habit.py`: Defines Habit and Periodicity with streak calculation
- `src/tracker.py`: Manages collection of habits and related operations
- `src/analytics.py`: Provides analytics on habit data and streaks
- `src/storage.py`: Handles saving/loading data with pickle
- `src/cli.py`: Command-line interface for interacting with the app
- `src/data_seed.py`: Script to pre-populate sample habit data for testing
- `src/tests/test_suite.py`: Unit tests covering core functionalities

## Getting Started

### Requirements
- Python 3.7 or higher

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/BenjerryX/habit-tracker.git
    cd New\ Habit\ tracker\ Project/src
    ```
2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```
3. Seed sample data (optional):
    ```bash
    python data_seed.py
    ```

### Running the Application
```bash
python cli.py
