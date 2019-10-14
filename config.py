class Config:
    pass


class DevelopmentConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = 0


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    pass
