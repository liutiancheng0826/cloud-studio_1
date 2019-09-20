#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
days=['Monday','Tuesday','Wednesday',
      'Thursday','Friday']
def get_time():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    
    return ip       
    
def calculator():
    
    return 
name = 'Liu' + \
       'Tian'+ \
       'cheng'
print "您好，欢迎来到 Cloud Studio"
print "当前时间是：" + get_time()
print "您的IP是：" + get_host_ip()
print '这是\'Alice\'的问候',
print days,
raw_input("please type in:\n")
#print calculator()
#cloud studio可以撤销，返回到上一补吗？
#cloud studio如何导出项目和文件？