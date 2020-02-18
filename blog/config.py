import os

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    JSON_SORT_KEYS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = "127.0.0.1:5000"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
