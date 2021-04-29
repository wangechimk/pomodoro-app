from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .main import views

app = Flask(__name__)
app.static_folder = 'static'
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
