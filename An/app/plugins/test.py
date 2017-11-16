#!/usr/bin/env python
# -*- coding:utf-8 -*-

import amqp_publisher





amqp_publisher.send2msg('_add_user', {'username': u'panyuanqing', 'host': u'192.168.75.6', 'password': u'rdyruryr', 'user': u'root'}, 14L)