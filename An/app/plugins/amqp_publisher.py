#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
        使用api ansible==1.9.2  生产者
'''
from amqplib import client_0_8 as amqp
import sys
import pickle
from app.models import Jobs
from app import db
from datetime import datetime


args = {'host':'192.168.75.6','user':'root','username':'zhangyage','password':'123456'}
yml_temp_name = '_add_user'
alias = 'zhang'

def send2msg(yml_temp_name,args,alias):
    conn = amqp.Connection(host="127.0.0.1:5672", userid="guest", password="guest", virtual_host="/", insist=False)
    chan = conn.channel()
    
    # cankao  http://blog.csdn.net/linvo/article/details/5750987
        #插入数据任务状态
    job = Jobs(
        object = alias,
        started = datetime.now(),
        finished = 0,
        template_name = yml_temp_name,
        args = pickle.dumps(args),
        status = 0
        )
    db.session.add(job)
    db.session.commit()
    id = job.id
    msg = (yml_temp_name,args,id)
    msg = amqp.Message(pickle.dumps(msg))
    msg.properties["delivery_mode"] = 2
    chan.basic_publish(msg,exchange="sorting_room",routing_key="json")

    chan.close()
    conn.close()
