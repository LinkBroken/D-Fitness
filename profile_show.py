import json


def show_profile(name): # A function that return the user's data 
    try:
        file = open(f"Workouts log/{name.title()}_log.json")
        if file: # if the file exists it json.load it then return 
            return json.load(file)
        return "No files found"
    except:
        return ("No Workouts yet")