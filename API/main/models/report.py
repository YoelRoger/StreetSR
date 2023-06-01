from datetime import datetime
from .. import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100), nullable=True)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # La relación entre Report y User se establece mediante la propiedad 'user_id' en Report.

    def __init__(self, description, location, photo, reported_date, resolved, user_id):
        self.description = description
        self.location = location
        self.photo = photo
        self.reported_date = reported_date
        self.resolved = resolved
        self.user_id = user_id
