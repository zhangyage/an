#!/usr/bin/env python
# -*- coding:utf-8 -*
'''表单'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo,IPAddress
from flask_wtf.file import file_allowed
from app.models import Group,Host

groups = Group.query.all()   #获取所有的组
hosts = Host.query.all()     #获取说有的主机


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
    

    


class SshkeyForm(FlaskForm):
    '''添加秘钥'''
    alias = StringField(label=u"alias",
                          validators=[DataRequired(u'Enter alias')],  #设置为必填项目
                          description=u"alias",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Alias",
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
    remote_password = PasswordField(label=u"remote_passwd",
                  validators=[DataRequired(u'Enter remote_passwd')],  #设置为必填项目
                  description=u"remote_passwd",
                  render_kw={"class":"form-control",
                             "id":"name",
                             "placeholder":"Enter remote_passwd",
                             #"required":"required"     #html提示不能为空
                      }
                  )
    submit = SubmitField(label=u"提交",
                         render_kw={"class":"btn btn-default",
                              }
                          )
    

class User_addForm(FlaskForm):
    '''添加用户'''
    alias = StringField(label=u"alias",
                          validators=[DataRequired(u'Enter alias')],  #设置为必填项目
                          description=u"alias",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Alias"                                     
                              }
                          )
    host_group = SelectField(label="Select Group / Host",
                  validators=[DataRequired('Select Group / Host')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.alias) for v in hosts],  #列表生成器生成选择 
                  description="Select Some Options",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id",
                             "placeholder":"Select Some Options"
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
    username = StringField(label=u"remote_user",
                      validators=[DataRequired(u'Enter remote_user')],  #设置为必填项目
                      description=u"remote_user",
                      render_kw={"class":"form-control",
                                 "id":"name",
                                 "placeholder":"Enter remote_user",
                                 #"required":"required"     #html提示不能为空
                          }
                      )
    password = PasswordField(label=u"remote_passwd",
                  validators=[DataRequired(u'Enter remote_passwd')],  #设置为必填项目
                  description=u"remote_passwd",
                  render_kw={"class":"form-control",
                             "id":"name",
                             "placeholder":"Enter remote_passwd",
                             #"required":"required"     #html提示不能为空
                      }
                  )
    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-default",
                              }
                          )


class User_delForm(FlaskForm):
    '''删除用户'''
    alias = StringField(label=u"alias",
                          validators=[DataRequired(u'Enter alias')],  #设置为必填项目
                          description=u"alias",
                          render_kw={"class":"form-control",
                                     "id":"name",
                                     "placeholder":"Enter Alias"                                     
                              }
                          )
    host_group = SelectField(label="Select Group / Host",
                  validators=[DataRequired('Select Group / Host')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.alias) for v in hosts],  #列表生成器生成选择 
                  description="Select Some Options",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id",
                             "placeholder":"Select Some Options"
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
    username = StringField(label=u"remote_user",
                      validators=[DataRequired(u'Enter remote_user')],  #设置为必填项目
                      description=u"remote_user",
                      render_kw={"class":"form-control",
                                 "id":"name",
                                 "placeholder":"Enter remote_user",
                                 #"required":"required"     #html提示不能为空
                          }
                      )    
    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-default",
                              }
                          )


class User_addpubForm(FlaskForm):
    '''通过密钥添加用户'''
    host_group = SelectField(label="Select Group / Host",
                  validators=[DataRequired('Select Group / Host')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.alias) for v in hosts],  #列表生成器生成选择 
                  description="Select Some Options",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id",
                             "placeholder":"Select Some Options"
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
    username = StringField(label=u"remote_user",
                      validators=[DataRequired(u'Enter remote_user')],  #设置为必填项目
                      description=u"remote_user",
                      render_kw={"class":"form-control",
                                 "id":"name",
                                 "placeholder":"Enter remote_user",
                                 #"required":"required"     #html提示不能为空
                          }
                      ) 
    host_group = SelectField(label="Key",
                  validators=[DataRequired('Select Key')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.alias) for v in hosts],  #列表生成器生成选择 
                  description="Select Some Options",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id",
                             "placeholder":"Select Keys"
                          }
                  )   
    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-default",
                              }
                          )
 


