#!/usr/bin/env python
# -*- coding:utf-8 -*

from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo,IPAddress
from flask_wtf.file import file_allowed
from app.models import Group

groups = Group.query.all()   #获取所有的标签


class GroupForm(FlaskForm):
    '''组添加'''
    group_name = StringField(label=u"组名",
                          validators=[DataRequired(u'请输入组名')],  #设置为必填项目
                          description=u"组名",
                          render_kw={"class":"form-control",
                                     "id":"name",                                     "placeholder":"Enter Name",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    description = StringField(label=u"描述",
                      validators=[
                          DataRequired(u'请输入组描述')
                        ],  #设置为必填项目
                      description=u"描述",
                      render_kw={"class":"form-control",
                                 "id":"description",
                            
                                 "placeholder":"Enter Description",
                                 #"required":"required"     #html提示不能为空
                          }
                      )
    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-default",
                              }
                          )
    
class HostForm(FlaskForm):
    '''主机添加'''
    alias = StringField(label=u"alias",
                          validators=[DataRequired(u'Enter alias')],  #设置为必填项目
                          description=u"alias",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Alias",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    ip1 = StringField(label=u"IP1",
                          validators=[DataRequired(u'Enter ip'),
                                      IPAddress(u"请输入正确的ip地址")
                                      ],  #设置为必填项目
                          description=u"IP1",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Ip",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    ip2 = StringField(label=u"IP2",
                          description=u"IP2",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Ip",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    port = StringField(label=u"port",
                          validators=[DataRequired(u'Enter port')],  #设置为必填项目
                          description=u"port",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Port",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    remote_user = StringField(label=u"remote_user",
                          validators=[DataRequired(u'Enter remote_user')],  #设置为必填项目
                          description=u"remote_user",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter remote_user",
                                     #"required":"required"     #html提示不能为空
                              }
                          )

    group_id = SelectField(label=u"所属组",
                  validators=[DataRequired(u'请选择标所属组')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.group_name) for v in groups],  #列表生成器生成选择 
                  description=u"所属组",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id"
                          }
                  )

    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-default",
                              }
                          )
    

    
#     hosts = SelectMultipleField(label=u"主机列表",
#                                 validators=[DataRequired(u'请选择主机')],
#                                 coerce = int,
#                                 choices = [(v.id,v.name) for v in auth_list],  #列表生成器生成选择
#                                 render_kw={"class":"form-control", 
#                                            "placeholder":u'请选择权限列表'
#                               })

 


