import os
from flask import Flask
from dotenv import load_dotenv
from flask_breadcrumbs import Breadcrumbs

#login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    Breadcrumbs(app=app)
    load_dotenv()
    app.config['API_URL'] = os.getenv('API_URL')
    #login_manager.init_app(app)
    from .routes import main, report, user, login, home
    #app.register_blueprint(routes.login.log)
    app.register_blueprint(routes.main.main)
    app.register_blueprint(routes.report.report)
    #app.register_blueprint(routes.repair.repair)
    app.register_blueprint(routes.user.user)
    app.register_blueprint(routes.home.home)
    return app