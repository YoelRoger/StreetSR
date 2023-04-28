#from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from ..maps import UserSchema
from ..models import ReportModel

"""class Report(Schema):
    id = fields.Int(dump_only=True)
    location = fields.Str(required=True)
    description = fields.Str(required=True)
    photo = fields.Str(required=True)
    reported_by = fields.Nested('users', many=False, exclude=('reports',))
    created_at = fields.DateTime(dump_only=True)
    is_resolved = fields.Bool(dump_only=True)
"""
class Report(SQLAlchemyAutoSchema):
    class Meta:
        model = ReportModel
        load_instance = True
        include_relationships = True
        include_fk = True


    reported_by = fields.Nested(UserSchema, exclude =('password_hash', 'user_type', 'reports',))
