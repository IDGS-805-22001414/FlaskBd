import os
from sqlalchemy import create_engine
import urllib


class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:tokis@127.0.0.1/bdidgs805'
    SQLALCHEMY_TRACK_MODIFICATIONS=False