from .__init__ import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # Creating the database Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __init__(self, username, age, weight, height, email, password,):
        self.username = username
        self.age = age
        self.weight = weight
        self.height = height
        self.email = email
        self.password = password

    # method for getting the weight
    def get_weight(self):
        return self.weight
    # method for getting the height
    def get_height(self):
        return self.height
