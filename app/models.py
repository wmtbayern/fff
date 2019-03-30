from app.exts import db

#models里面主要就是创建模型,导入数据库就可以了,

class User(db.Model):
    #flask 里面一定要设置主键,不像 Django会自动创建
    #类似Django 的class Meta: 给表重命名
    __tablename__='user'
    #注意各个字段的书写,限制字段的书写
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    password=db.Column(db.String(80))