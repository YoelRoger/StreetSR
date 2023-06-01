from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from .report import Report


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)
    reports = db.relationship('Report', backref='user', lazy=True)
    
    def __init__(self, name, email, dni, password, user_type):
        self.name = name
        self.email = email
        self.dni = dni
        self.password = password
        self.user_type = user_type
