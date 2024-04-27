# Import necessary modules
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()
database_name = "database.db"

# Function to create the Flask application
def create_app():
    # Create Flask application instance
    app = Flask(__name__)
    # Set secret key for the application
    app.config['SECRET_KEY'] = "Secret Key"
    # Set the URI for the SQLite database
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_name}"

    # Initialize SQLAlchemy with the Flask application
    db.init_app(app)

    # Import views and authentication blueprints
    from .views import views
    from .auth import Auth

    # Register blueprints with the Flask application
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(Auth, url_prefix="/")

    # Import the User model
    from .models import User

    # Create the database if it doesn't exist
    create_database(app)

    # Initialize LoginManager for handling user authentication
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # Callback function to load a user from the database
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Function to create the database
def create_database(app):
    with app.app_context():
        db.create_all()
