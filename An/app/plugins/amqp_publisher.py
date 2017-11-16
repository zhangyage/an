#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
        使用api ansible==1.9.2  生产者
'''
from amqplib import client_0_8 as amqp
import sys
import pickle
from model import Jobs
from datetime import datetime


# args = {'host':'192.168.75.6','user':'root','username':'zhangyage','password':'123456'}
# yml_temp_name = '_add_user'
# alias = 'zhang'

def send2msg(yml_temp_name,args,alias):
    conn = amqp.Connection(host="127.0.0.1:5672", userid="guest", password="guest", virtual_host="/", insist=False)
    chan = conn.channel()
    
    # cankao  http://blog.csdn.net/linvo/article/details/5750987
        #插入数据任务状态
    print 0
    job = Jobs()
    id = job.Insdate(object=alias, started=datetime.now(), finished="0", template_name=yml_temp_name, args=pickle.dumps(args), status=0)
    print 1    
    msg = (yml_temp_name,args,id)
    print msg
    msg = amqp.Message(pickle.dumps(msg)) 
    msg.properties["delivery_mode"] = 2
    chan.basic_publish(msg,exchange="sorting_room",routing_key="json")

    chan.close()
    conn.close()

# if __name__ == "__main__":
#    send2msg(yml_temp_name,args,alias)
