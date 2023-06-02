import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager



db = SQLAlchemy()
ma = Marshmallow()
api = Api()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
        'DATABASE_PASSWORD') + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') + '/' + os.getenv(
        'DATABASE_NAME')
    db.init_app(app)
    ma.init_app(app)


    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    #from main.auth import auth
    #app.register_blueprint(auth.auth)

    # Importamos los endpoints(resources)
    from main.resources import user_resource
    api.add_resource(user_resource.UsersResource, '/users')
    api.add_resource(user_resource.UserResource, '/user/<id>')
    from main.resources import report_resource
    api.add_resource(report_resource.ReportsResource, '/reports')
    api.add_resource(report_resource.ReportResource, '/reports/<id>')
    api.init_app(app)

    return app





