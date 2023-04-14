from marshmallow import Schema, fields
# from .user import UserSchema


class Report(Schema):
    id = fields.Int(dump_only=True)
    location = fields.Str(required=True)
    description = fields.Str(required=True)
    photo = fields.Str(required=True)
    reported_by = fields.Nested('users', many=False, exclude=('reports',))
    created_at = fields.DateTime(dump_only=True)
    is_resolved = fields.Bool(dump_only=True)
