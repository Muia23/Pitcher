from flask import Flask
from config import config_options

def create_app(config_name):

    #Initializing app
    app = Flask(__name__)    

    #create app config
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    return app