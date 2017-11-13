#coding:utf8

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://zhangyage:Zhang123@47.94.188.237/ansible"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
app.config["ANSIBLE_KEY"] = '/root/.ssh/id_rsa.pub'
app.config["AMQP"] = '''host="127.0.0.1:5672", userid="guest", password="guest", virtual_host="/", insist=False'''

db = SQLAlchemy(app)
app.debug = True

from app.admin import admin as admin_blueprint   #导入蓝图
app.register_blueprint(admin_blueprint)    #注册蓝图

