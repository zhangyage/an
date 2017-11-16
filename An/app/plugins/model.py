#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sql_helper import MySqlHelper
import datetime

#任务状态数据存入表
class Jobs:
    def __init__(self):
        self.sqlHelper = MySqlHelper()  
       
    def Insdate(self,object,started,finished,template_name,args,status):
        '''插入任务记录
        @param object:操作对象
        @param started:开始时间
        @param finished:结束时间
        @param template_name:操作模板
        @param args:参数
        @param status:状态  0未知 1完成 2失败
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into jobs(object,started,finished,template_name,args,status) values(%s,%s,%s,%s,%s,%s)'
        params = (object,started,finished,template_name,args,status)
        result = self.sqlHelper.InsSample_ReturnId(sql, params)
        return result
            
    def Simple_update(self,finished,status,id):
        '''
            @修改任务状态信息
        '''
        sql = "update jobs set finished=%s,status=%s where id =%s"
        params = (finished,status,id)
        result = self.sqlHelper.Update_Sample(sql, params)
        print result

        
        


    
    