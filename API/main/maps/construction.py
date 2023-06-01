from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from main.models.construction import Construction
from ..maps import UserSchema


class ConstructionSchema(SQLAlchemyAutoSchema):
    user_id = fields.Nested(UserSchema, exclude=('password', 'user_type', 'reports',))

    class Meta:
        model = Construction
        load_instance = True
        include_relationships = True
        include_fk = True

