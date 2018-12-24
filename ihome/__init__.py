# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis

# 导入蓝图
from ihome import api_1_0

# 数据库
db = SQLAlchemy()

# redis 连接对象
redis_store = None


# 工厂模式
def Create_App(config_name):
    """
    创建flask的应用模式对象
    :param config_name:str 配置模式名("develop","product")
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config = config_map.get(config_name)
    app.config.from_object(config)

    # app 初始化db
    db.init_app(app)
    # redis 初始化
    global redis_store
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    # 利用flask_session 将session 保存到redis
    Session(app)
    # 为flask补充csrt防护
    CSRFProtect(app)

    # 注册蓝图
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    return app
