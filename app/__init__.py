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

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    ## setting config
    #from .requests import configure_request
    #configure_request(app)

    return app