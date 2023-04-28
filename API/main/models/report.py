from datetime import datetime
from .. import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200), nullable=False)  # ver LargeBinary
    reported_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_resolved = db.Column(db.Boolean, default=False)
    user = db.relationship("User", foreign_keys=[reported_by], back_populates="reports", uselist=False, single_parent=True)


    def __repr__(self):
        return f"<Report {self.id}>"
