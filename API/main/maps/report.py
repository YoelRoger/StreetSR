#from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from ..maps import UserSchema
from ..models import ReportModel


class Report(SQLAlchemyAutoSchema):
    user_id = fields.Nested(UserSchema, exclude =('password', 'user_type', 'reports',))

    class Meta:
        model = ReportModel
        load_instance = True
        include_relationships = True
        include_fk = True


