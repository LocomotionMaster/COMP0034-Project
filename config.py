from os.path import dirname, abspath, join


class Config(object):
    SECRET_KEY = 'fejfhefjheft7etguwfh'

    DEBUG = False
    TESTING = False

    CWD = dirname(abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'langbridge.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True


class DevConfig(Config):
    DEBUG = True