import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'dejan.luznic@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_SUPPRESS_SEND = False
    SECRET_KEY = 'utjglfjmvsnsk$$%js'
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'


class ProductionConfig(Config):
    '''
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
    DATABASE_PORT = ''
    DATABASE_NAME = ''
    DATABASE_HOST = ''
    DATABASE_URI = 'mysql+mysqlconnector://'
    '''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rtrades123@127.0.0.1/rtrade'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SECRET_KEY = 'ksjsgksngsngijrgjng'