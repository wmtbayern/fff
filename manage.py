
# from flask_script import Manager
#
# from app import create_app
#
# app=create_app()
#
# manager=Manager(app)
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app

app=create_app()
#manage.py文件基本上就是设置manager,是项目的入口
manager=Manager(app)

migrate=Migrate(app)
#namager 接收命令行参数,'db',替换成 MigrateCommand

manager.add_command('db',MigrateCommand )

if __name__ == '__main__':

    manager.run()
