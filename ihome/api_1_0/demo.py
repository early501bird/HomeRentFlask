# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_
from . import api

@api.route("/index")
def index():
    return "index page"

