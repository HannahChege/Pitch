import os

class Config:
    SECRET_KEY = 'scarletshevannah'
    
UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hannah:hannah@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}