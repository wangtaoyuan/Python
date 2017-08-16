# encoding:utf-8
'''
Created on 2017年8月7日
题目：暂停一秒输出，并格式化当前时间。
知识链接：
    1、时间和日期 库 http://www.runoob.com/python/python-date-time.html
    
@author: wangtaoyuan
'''
import time
time1 = time.strftime("%Y.%m.%d %p %I:%M:%S  ",time.localtime())
time.sleep(1)
print time1