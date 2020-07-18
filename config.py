import os

class Config:
    '''
    Class configuration class
    '''
    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://willy:willy@localhost/soi'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options= {
'development' :DevConfig,
'production':ProdConfig
}