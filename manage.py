# !c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python3.6
# _*_ coding:utf-8 _*_
from ihome import Create_App, db
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

app = Create_App("develop")
manager = Manager(app)
Migrate(app, db)

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
