from datetime import datetime
from .. import db


class Construction(db.Model):
    __tablename__ = 'constructions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    report_ids = db.relationship('Report', backref='construction', lazy=True)

    def __init__(self, description, location, start_date, end_date, user_id):
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
