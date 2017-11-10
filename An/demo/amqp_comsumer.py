#!/usr/bin/env python
# -*- coding:utf-8 -*-
from amqplib import client_0_8 as amqp
import sys

conn = amqp.Connection(host="192.168.75.7:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

chan.queue_declare(queue="po_box", durable=True,  exclusive=False, auto_delete=False)  
chan.exchange_declare(exchange="sorting_room", type="direct", durable=True,  auto_delete=False,) 
# cankao  http://blog.csdn.net/linvo/article/details/5750987
chan.queue_bind(queue="po_box", exchange="sorting_room", routing_key="json")

def recv_callback(msg):  
    print 'Received: ' + msg.body  
chan.basic_consume(queue='po_box', no_ack=True,callback=recv_callback, consumer_tag="testtag")  
while True:  
    chan.wait()  
chan.basic_cancel("testtag") 
chan.close()
conn.close()
