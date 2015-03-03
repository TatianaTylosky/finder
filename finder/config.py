import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://tati:tati@localhost:5432/finder"
    DEBUG = True
