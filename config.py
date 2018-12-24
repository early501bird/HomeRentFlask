# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_
import redis


class Config(object):
    # DEBUG = True
    SECRET_KEY = "bGl3ZWlsaXdlaQ=="
    # database
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome20181224"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # flask_session
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


"""开发模式"""


class DevlopmentConfig(Config):
    DEBUG = True
    pass


"""线上生成模式"""


class ProductConfig(Config):
    DEBUG = False
    pass


config_map = {
    "develop": DevlopmentConfig,
    "product": ProductConfig
}
