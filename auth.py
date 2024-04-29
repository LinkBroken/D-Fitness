# Import necessary modules and libraries
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user

# Import database models and email validation module
from .models import *
import re
from .email_validation import *

# Create a Blueprint named "auth"
Auth = Blueprint("auth", __name__)

# Route for user login
@Auth.route("/login", methods=["GET", "POST"])
def login():
    # Check if the database exists
    if db:
        # Check if the request method is POST
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            user = User.query.filter_by(email=email).first()
            # Check if email field is empty
            if email == "":
                flash("empty email, fill it please", category="error")
            elif user:
                # Check if password field is empty or password is incorrect
                if user.password == "":
                    flash("empty password, fill it please", category="error")
                elif user.password != password:
                    flash("Wrong password", category="error")
                else:
                    # Log in the user and redirect to home page
                    login_user(user, remember=True)
                    return redirect(url_for("views.home"))
            else:
                # Validate email format
                if not validate(email):
                    flash("Invalid email", category="error")
    # Render login template
    return render_template("authentications/SignIn.html")

# Route for user registration
@Auth.route("/register", methods=["GET", "POST"])
def signup():
    # Check if the database exists
    if db:
        # Check if the request method is POST
        if request.method == "POST":
            username = request.form["name"]
            email = request.form["email"]
            age = request.form["age"]
            height = request.form["height"]
            weight = request.form["weight"]
            password = request.form["password"]
            # Check for empty fields and existing username and email
            if email == "":
                flash("Please provide an email.", category="error")
            elif not validate(email):
                flash("Invalid Email", category="error")
            elif password == "":
                flash("Please provide a password.", category="error")
            elif username == "":
                flash("Please provide a username.", category="error")
            elif User.query.filter_by(username=username).first() is not None:
                flash("username already exists. Please choose another one.", category="error")
            elif User.query.filter_by(email=email).first() is not None:
                flash("Email already exists. Please choose another one.", category="error")
            else:
                # Create a new user and add to the database
                new_user = User(username=username, age=age, weight=weight, height=height, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                # Go the log in page after signing up
                return redirect(url_for("auth.login"))
    # Render registration template
    return render_template("authentications/Signup.html")

# Route for user logout
@Auth.route("/logout")
def logout():
    # Log out the user and redirect to login page
    logout_user()
    return redirect(url_for("auth.login"))
