from marshmallow import Schema, fields
from ..maps import ReportSchema


# Schema
class User(Schema):
    id = fields.Int(dump_only=True)  # Read from db only
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    user_type = fields.Bool(required=True)
    reports = fields.Nested('reports', many=True, exclude=('user',))
