#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
     @存放数据模型
     @配置参考：http://www.pythondoc.com/flask-sqlalchemy/
'''
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://zhangyage:Zhang123@47.94.188.237/ansible"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
'''
from datetime import datetime
from app import db

#用户表或管理员表
class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 昵称
    password = db.Column(db.String(100))  # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    active = db.Column(db.SmallInteger)  # 用户状态，1为活跃，0为禁用
    userlogs = db.relationship("Userlog", backref='user')
    oplogs = db.relationship("Oplog", backref='user')
    
    
    def __repr__(self):
        return "<User %r>" % self.username
    
    def check_pwd(self, pwd):     #密码认证模块
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)
    
    


    

# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 角色权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    users = db.relationship("User", backref='role')  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name
    
# 管理员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id
    
# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<Oplog %r>" % self.id

    
#主机表    
class Host(db.Model):
    __tablename__="host"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    alias = db.Column(db.String(255), unique=True)  #别名    也可以叫做主机名
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))  # 所属组
    ip1 = db.Column(db.String(100))                 #IP地址1
    ip2 = db.Column(db.String(100))                 #Ip地址2
    port = db.Column(db.SmallInteger)               #远程端口号
    remote_user = db.Column(db.String(255))         #远程用户名
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  #添加时间
    
    def __repr__(self):
        return "<Host %r>" % self.id
    
#主机组    
class Group(db.Model):
    __tablename__="group"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    group_name = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  #添加时间
    hosts= db.relationship("Host", backref='group')
    
    def __repr__(self):
        return "<Group %r>" % self.id
    
#任务表
class Jobs(db.Model):
    __tablename__="jobs"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    started = db.Column(db.SmallInteger)  # 用户状态，1为活跃，0为禁用
    finished = db.Column(db.SmallInteger)  # 用户状态，1为活跃，0为禁用
    template_name = db.Column(db.String(255), unique=True)
    args = db.Column(db.String(255))
    status = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  #添加时间

'''    
if __name__ == "__main__":
    db.create_all()          #创建数据库
    
    role = Role(
        name = "超级管理员",
        auths=""
    )
    db.session.add(role)
    db.session.commit()
    
    from werkzeug.security import generate_password_hash
    user = User(
        username="zhangyage",
        password=generate_password_hash("123456"),
        active=1,
        role_id=1
    )
    db.session.add(user)
    db.session.commit()
'''

