#!/usr/bin/env python
# -*- coding:utf-8 -*-
from amqplib import client_0_8 as amqp
import sys
import pickle

args = {'host':'192.168.75.6','user':'root','username':'zhangyage','password':'123456'}
yml_temp_name = '_add_user'

conn = amqp.Connection(host="127.0.0.1:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

# cankao  http://blog.csdn.net/linvo/article/details/5750987

msg = (yml_temp_name,args)
msg = amqp.Message(pickle.dumps(msg))
msg.properties["delivery_mode"] = 2
chan.basic_publish(msg,exchange="sorting_room",routing_key="json")

chan.close()
conn.close()
