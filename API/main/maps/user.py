# from marshmallow import Schema, fields
# from ..maps import ReportSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import UserModel

# Schema
"""class User(Schema):
    id = fields.Int(dump_only=True)  # Read from db only
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    user_type = fields.Bool(required=True)
    reports = fields.Nested('reports', many=True, exclude=('user',))
"""


class User(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        include_fk = True
