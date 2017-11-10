from amqplib import client_0_8 as amqp
import sys

conn = amqp.Connection(host="192.168.75.7:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

# chan.queue_declare(queue="po_box", durable=True,  exclusive=False, auto_delete=False)  
# chan.exchange_declare(exchange="sorting_room", type="direct", durable=True,  auto_delete=False,) 
# cankao  http://blog.csdn.net/linvo/article/details/5750987

#msg = amqp.Message(sys.argv[1])
msg = amqp.Message('zhangyage')
msg.properties["delivery_mode"] = 2
chan.basic_publish(msg,exchange="sorting_room",routing_key="json")

chan.close()
conn.close()