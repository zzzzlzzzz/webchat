from os import environ


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('WEBCHAT_DATABASE_URI', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = 0


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    pass
