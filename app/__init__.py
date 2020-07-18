from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    #Initialize the app
    app = Flask(__name__)    

    #create app config
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #Initialize flask extention
    bootstrap.init_app(app)
    db.init_app(app)

    return app