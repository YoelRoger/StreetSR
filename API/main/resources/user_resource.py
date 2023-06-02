from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError

from ..maps import UserSchema
from ..repositories import UserRepository

user_schema = UserSchema()
user_repository = UserRepository()


class UserResource(Resource):
    def get(self, id):
        # buscar el usuario en el repositorio
        user = user_repository.get_by_id(id)

        # devolver el usuario encontrado o un mensaje de error si no se encontró
        if user:
            return user_schema.dump(user)
        else:
            return {'message': 'Usuario no encontrado'}, 404

    def post(self):
        request_data = request.get_json()

        try:
            # validar el cuerpo de la solicitud con el esquema de usuario
            user = user_schema.load(request_data)
        except ValidationError as e:
            raise BadRequest(str(e))

        # crear el usuario en el repositorio
        created_user = user_repository.create(user)

        # devolver el usuario creado con el código de estado 201 CREATED
        return user_schema.dump(created_user), 'USUARIO CREADO', 201

    def delete(self, id):
        user = user_repository.get_by_id(id)

        if not user:
            return {'message': 'User not found'}, 404

        user_repository.delete(user)
        return 'USUARIO ELIMINADO', 204


class UsersResource(Resource):
    # Obtener recursoS

    def get(self):
        users = user_repository.get_all()
        return user_schema.dump(users, many=True)
