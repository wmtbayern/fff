from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models import User
#因为blue在views 里面用到,所以蓝图在这里实例化,并完成注册
from app.exts import db

blue=Blueprint('blue',__name__)  #'blue' 在反向解析的时候会用到

#写函数,让__init__.py 导入,这样才可以建立关联

def init_view(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')

def index():
    name=session.get('username','游客')
    return render_template('index.html',name=name)

@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')

        #状态保持
        session['username']=username

        return redirect(url_for('blue.index'))

@blue.route('/register/',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    elif request.method=='POST':
        pass

@blue.route('/logout/')
def logout():
    #方式一: session 依赖于cookies 删除cookies 就可以
    # response=redirect(url_for('blue.index'))
    # response.delete_cookie('session')
    # 方式二: 只是注销session
    session.pop('username')
    return redirect(url_for('blue.index'))

@blue.route('/createall/')
def createall():
    db.create_all()

    return '创建成功'