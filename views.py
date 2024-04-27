# importing the needed functions
from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required, current_user
from .__init__ import db
from datetime import datetime
import calendar
from .exercises_log import log_workout
from .profile_show import show_profile

views = Blueprint("views", __name__) # creating the blueprints

@views.route("/") # routing the home page
@login_required
def home():
    return render_template("home.html", user= current_user.username) # renders the "home.html" page  with "user" as an additional parameter

@views.route("/trainer") # routing the muscle group (trainer) page
@login_required
def trainer():
    return render_template("trainer.html", user=current_user.username)

@views.route("/profile") # The profile page route
def profile():
    today = datetime.today() # The current clock time the user's in
    logs = show_profile(current_user.username) # uses the show_profile function with the signed in user as an argument, for more explainion go the profile_show.py file
    workout_day = f"{today.day} {calendar.month_name[today.month]} {today.year}" # the current date the user's in 
    if logs: # if the user has any logs
        if request.method == "POST":
            try:
                len_logs = len(logs)
                day = int(request.form["day"])
                month = int(request.form["month"])
                year = int(request.form["year"])
                workout_day = f"{day} {calendar.month_name[month]} {year}" # After taking the date's inputs from the user, it creates a variable with given values and stores it in the workout_day variable
                if workout_day:
                    pass
                else:
                    return render_template("profile.html")
            except: # if the user's input is empty or has letters they get redirect into the profile page
                return redirect("/profile")
    len_logs = 0
    return render_template("profile.html", user=current_user, showing = logs, length = len_logs, day=workout_day)

@views.route("/<exercise>",methods=['GET','POST']) # a dynamic route with GET and POST methods
@login_required
def exercise(exercise):
    try:
        if request.method == "POST":
            exercise_name = request.form["exercise"] # retrieving the exercise name
            try: # checking if the sets and reps are numbers
                sets = int(request.form["sets"])
                reps = int(request.form["reps"])
                log_workout(current_user.username,exercise, exercise_name,sets,reps) # using the log_workout function, more explaination on the exercises_log.py file
            except:
                flash("sets and reps are numbers", category="error")
            return redirect(url_for("views.profile"))
        return render_template(f"{exercise}.html")
    except: # If the route doesn't exist, the user will go to the error page
        return render_template("errorPage.html")