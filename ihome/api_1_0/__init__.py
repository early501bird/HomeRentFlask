# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_

from flask import Blueprint


# 创建蓝图对象
api = Blueprint('api_1_0', __name__)

#导入蓝图,注意这个顺序不能错
from . import demo