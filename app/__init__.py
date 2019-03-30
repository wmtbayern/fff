from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.exts import init_ext
from app.settings import init_app
from app.views import blue, init_view

# init.py 文件主要是起到创建定义一个函数创建app,初始化配置的作用

def create_app( env_name='default'):
    #实例化一个  Flask 对象,
    app = Flask(__name__)
    #注意初始化的顺序,init_app(),一定是在其他初始化的前面
    init_app(app,env_name)
    init_ext(app)
    #session存储类型一定要备注,否则用不了session
    # app.config['SESSION_TYPE']='redis'
    # 初始化，方式一
    # Session(app)
    # 初始化，方式二
    # sess = Session()
    # sess.init_app(app)
    #相对路径: ///  相对于当前文件的路径
    #绝对路径: ////  相对于根目录的路径,从根目录开始的路径
    # 传入 参数 app, 此时 views.py 里面才有app
    init_view(app)
    return app