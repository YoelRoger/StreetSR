from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from ..maps import ReportSchema
from ..repositories import ReportRepository

report_schema = ReportSchema()
report_repository = ReportRepository()


class ReportResource(Resource):
    # Obtener reporte por ID
    def get(self, reported_by):
        report = report_repository.get_by_reported_by(reported_by)
        if report:
            result = report_schema.dump(report)
            return result, 200
        else:
            return {'message': 'Reporte no encontrado'}, 404

    # Actualizar reporte por ID
    def put(self, id):
        report = report_repository.get_by_id(id)
        if report is None:
            return {'message': 'Report not found'}, 404

        # Parse request data
        data = request.get_json()
        errors = report_schema.validate(data)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, 400

        # Update report
        updated_report = report_repository.update(id, data)

        # Serialize and return updated report
        result = report_schema.dump(updated_report)
        return {'message': 'Report updated', 'data': result}, 200

    # Eliminar reporte por usuario
    def delete(self, reported_by):
        report = report_repository.get_by_reported_by(reported_by)
        if report:
            report_repository.delete(report)
            return 'REPORTE ELIMINADO', 204
        else:
            return {'message': 'Reporte no encontrado'}, 404
