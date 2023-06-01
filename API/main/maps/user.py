from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import UserModel


class User(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        include_fk = True

