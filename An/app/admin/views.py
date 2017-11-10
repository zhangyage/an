#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import admin
from flask import render_template,url_for,request,session,flash,redirect
from app.admin.form import GroupForm,HostForm
from app.models import Group,Host
from app import db

@admin.route("/")
def index():
    return render_template("base.html")


@admin.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")

#添加主机
@admin.route("/host_add/", methods=["GET","POST"])
def host_add():
    form = HostForm()
    if form.validate_on_submit():
        data = form.data
        host = Host.query.filter_by(alias=data["alias"]).count() #不可以有重复标签
        if host == 1:
            flash(u"别名已存在！",'err')
            return redirect(url_for('admin.host_add'))
        host = Host(
            alias=data["alias"],
            ip1=data["ip1"],
            ip2=data["ip2"],
            port=data["port"],
            remote_user=data["remote_user"],
            group_id=int(data["group_id"])
        )
        db.session.add(host)   #添加数据
        db.session.commit()   #提交数据
        flash(u"添加成功！", "OK")
    return render_template("host_add.html",form=form)


#主机列表
@admin.route("/host_list/<int:page>/", methods=["GET"])
def host_list(page=None):
    if page is None:
        page = 1
    page_data = Host.query.join(
        Group
        ).filter(
            Host.group_id == Group.id
        ).order_by(
        Host.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("host_list.html",page_data=page_data)

#查看主机信息
@admin.route("/host_view/<int:id>/", methods=["GET"])
def host_view(id=None):
    return render_template("host_view.html",id=id)

#查看主机信息
@admin.route("/host_edit/<int:id>/", methods=["GET","POST"])
def host_edit(id=None):
    form = HostForm()
    host = Host.query.get_or_404(id)
    if request.method == "GET":
        form.group_id.data = host.group_id
    if form.validate_on_submit():
        data = form.data
        host_count = Host.query.filter_by(alias=data["alias"]).count()
        if host_count == 1 and host.alias != data["alias"]:
            flash(u"修改失败",'err')
            return redirect(url_for('admin.host_edit',id=id))
        
        host.alias = data["alias"],
        host.ip1 = data["ip1"],
        host.ip2 = data["ip2"],
        host.port = data["port"],
        host.remote_user = data["remote_user"],
        host.group_id = data["group_id"]
        db.session.add(host)
        db.session.commit()
        flash(u"修改主机信息成功",'OK')
        return redirect(url_for('admin.host_edit',id=id))
    return render_template("host_edit.html",form=form,host=host)


#删除主机
@admin.route("/host_del/<int:id>/", methods=["GET","POST"])
def host_del(id=None):
    host=Host.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(host)
    db.session.commit()
    flash(u"删除主机成功", "OK")
    return redirect(url_for('admin.host_list',page=1))



#添加组
@admin.route("/group_add/", methods=["GET","POST"])
def group_add():
    form = GroupForm()
    if form.validate_on_submit():
        data = form.data
        group = Group.query.filter_by(group_name=data["group_name"]).count() #不可以有重复标签
        if group == 1:
            flash(u"组名已存在！",'err')
            return redirect(url_for('admin.group_add'))
        group = Group(
            group_name=data["group_name"],
            description=data["description"]
        )
        db.session.add(group)   #添加数据
        db.session.commit()   #提交数据
        flash(u"添加成功！", "OK")
    return render_template("group_add.html",form=form)


#组列表
@admin.route("/group_list/<int:page>/", methods=["GET"])
def group_list(page=None):
    if page is None:
        page = 1
    page_data = Group.query.join(
        Host
        ).filter(
            Group.id == Host.group_id,
        ).order_by(
        Group.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
#     for i in page_data.items:
#         for j in i.hosts:
#             print j.alias
    return render_template("group_list.html",page_data=page_data)