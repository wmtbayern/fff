

class BaseConfig(object):
    # 直接 赋值 的形式
    SECRET_KEY = '@#EJdfds_njasnDHGSAHWEIUcnskd1122435%hj7&&&^%^jkvd"><'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    SESSION_TYPE ='redis'

#先有一个基本的配置,各个环境相同的配置放一起,之后继承,或重写

#每个环境不一样的配置再重写就可以了

class DevelopConfig(BaseConfig):
    DEBUG=True
    #注意路径的写法,
    #/// 相对路径      ////  绝对路径
    SQLALCHEMY_DATABASE_URI = 'sqlite:///develop.db'

class TestingConfig(BaseConfig):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'

class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///staging.db'

class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///product.db'



config={
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}

def init_app(app,env_name):

    # app.config.from_object(config.get(env_name))
    # app.config.from_object(config.get(env_name))
    # app.config.from_object(config.get(env_name))
    # app.config.from_object(config.get(env_name))
    # app.config.from_object(config.get(env_name))
    app.config.from_object(config.get(env_name))