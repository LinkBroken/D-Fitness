# Importing necessary modules for logging workouts
from datetime import datetime
import os
import json
import calendar

# Function to log a workout
def log_workout(name, muscle, exercise, sets, reps):
    # Create directory for workout logs if it doesn't exist
    directory = "Workouts log"
    os.makedirs(directory, exist_ok=True)

    # Get current date
    today = datetime.today()

    # Define workout details
    Workout = {
        f"{today.day} {calendar.month_name[today.month]} {today.year}":
            {
                "muscle targeted": muscle,
                "exercise": exercise,
                "sets": sets,
                "reps": reps,
            }
    }

    # Create file path for the workout log
    file_path = os.path.join(directory, f"{name.title()}_log.json")

    # Check if the log file exists and load existing data
    if os.path.exists(file_path):
        with open(file_path, "r") as open_file:
            workout_list = json.load(open_file)
    else:
        workout_list = []

    # Append new workout to the list
    workout_list.append(Workout)

    # Write updated workout list to the log file
    with open(file_path, "w") as open_file:
        json.dump(workout_list, open_file, indent=4, separators=[",", ":"])
