#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
#from app import db,app
from models import Host,Group

try:
    import json
except ImportError:
    import simplejson as json


def hosts_group():
    mockData={}
    hosts_group = Host.query.join(
        Group
        ).filter(
        Host.group_id == Group.id
        ).all()
    for host in hosts_group:
        if not  mockData.has_key(host.group.group_name):
            mockData[host.group.group_name]={'hosts':[host.ip1]}
        else:
            mockData[host.group.group_name]['hosts'].append(host.ip1)
    #mockData=json.dumps(mockData,indent=4)
    return mockData



# '''这里是模拟数据，工作上一般该数据都是从数据库或者缓存中读取的'''
# mockData = {
#     "web":{
#         "hosts": ["192.168.75.6"],
#         "vars":{
#             "http_port":8888,
#             "max_clients":789
#         }
#     },
# "db":{
#         "hosts":["192.168.75.3"],
#         "vars":{
#             "action":"Restart MySQL server."
#         }
#     }
# }
'''模拟数据结束'''
def getList():
    '''get list hosts group'''
    print json.dumps(mockData)


def getVars(host):
    '''Get variables about a specific host'''
    print json.dumps(mockData[host]["vars"])


if __name__ == "__main__":
    mockData = hosts_group()
    parser = argparse.ArgumentParser()
    parser.add_argument('--list',action='store_true',dest='list',help='get all hosts')
    parser.add_argument('--host',action='store',dest='host',help='get all hosts')
    args = parser.parse_args()

    if args.list:
        getList()

    if args.host:
        getVars(args.host)
    
    

