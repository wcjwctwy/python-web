import asyncio, logging

from flask_sqlalchemy import SQLAlchemy

from www.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:890610@10.20.7.23:3306/python?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class UserData(db.Model):
    __tablename__ = 'tab_user'
    id = db.Column(db.INT(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20), default="")
    email = db.Column(db.String(20), default="")

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return 'username:%s,password:%s,email:%s' % (self.username,self.password,self.email)


db.create_all()
