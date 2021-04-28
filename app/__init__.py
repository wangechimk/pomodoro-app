from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.static_folder = 'static'
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app.config.from_object(config_options[config_name])

    bootstap.init_app(app)

    return app