from .. import db
from ..models import ReportModel


# Repository
class Report:
    def __init__(self):
        self.reports = ReportModel

    def get_all(self):
        return self.reports.query.all()

    def get_by_id(self, id):
        return self.reports.query.get(id)

    def get_by_reported_by(self, reported_by):
        return self.reports.query.filter_by(name=reported_by).all()

    def create(self, report):
        db.session.add(report)
        db.session.commit()
        return report

    def update(self, id, data):
        report = self.reports.query.get(id)
        for key, value in data:
            setattr(report, key, value)
        db.session.add(report)
        db.session.commit()
        return report

    def delete(self, id):
        report = self.reports.query.get(id)
        db.session.delete(report)
        db.session.commit()
        return report
