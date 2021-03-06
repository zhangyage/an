#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
        使用api ansible==1.9.2  消费者
'''
import ansible.playbook
from ansible import callbacks
from ansible import utils
from amqplib import client_0_8 as amqp
import sys
import pickle
import os
import json


#def ansible_book(db, pb, args):
def ansible_book(pb, args):
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
    playbook = ansible.playbook.PlayBook(
        playbook=pb,                    #要执行的剧本
        extra_vars=args,                #剧本中设置的变量传递
        stats=stats,                    #必填参数
        callbacks=playbook_cb,          #必填参数
        runner_callbacks=runner_cb,     #必填参数
        #check=True                     #测试执行，设置为这个True的时候只会输出执行结果   但是不会在真实服务器上执行
    )
    result = playbook.run()
    result = json.dumps(result,indent=4)
    return result

def recv_callback(msg):                 #获取消息传来的值作为参数处理 
    yml_temp_name, args = pickle.loads(msg.body)
    pb = os.path.join(os.path.join('/root', yml_temp_name), 'main.yml')   #拼合剧本路径
    print pb
    print args
    status = ansible_book(pb, args)
    print  status
    

conn = amqp.Connection(host="127.0.0.1:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

chan.queue_declare(queue="po_box", durable=True,  exclusive=False, auto_delete=False)     #设置对列
chan.exchange_declare(exchange="sorting_room", type="direct", durable=True,  auto_delete=False,)  #设置交换机
# cankao  http://blog.csdn.net/linvo/article/details/5750987
chan.queue_bind(queue="po_box", exchange="sorting_room", routing_key="json")      #绑定对列和交换进

#def recv_callback(msg):  
#    print 'Received: ' + msg.body  
#    msg = pickle.loads(msg.body)
#    print msg
#    status = recv_callback(msg)
#    print status

chan.basic_consume(queue='po_box', no_ack=True,callback=recv_callback, consumer_tag="testtag")  
while True:  
    chan.wait()  
chan.basic_cancel("testtag") 
chan.close()
conn.close()

