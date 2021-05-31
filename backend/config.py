from os import environ, path
from dotenv import load_dotenv

# base directory path
basedir = path.abspath(path.dirname(__file__))

# load environment variables file
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config"""

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """ production config """

    ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    """ development config """

    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')


class TestConfig(DevConfig):
    """ testing config """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')
