# encoding:utf-8
'''
Created on 2017年8月10日
题目：输出指定格式的日期。
知识链接：
    1、re.finditer-正则取字符串中的数字(正则切片)：
        a = re.finditer(r'\d+', str)
        print a.group()
    2、time.localtime()、time.strftime('格式', time.localtime())
@author: wangtaoyuan
'''
import datetime
import time
import re
time = time.strftime('%Y, %m, %d, %H, %M, %S',time.localtime())
ti = []
for i in re.finditer(r'\d+', time):
    ti.append(int(i.group()))
date = datetime.datetime(ti[0], ti[2], ti[2], ti[3], ti[5])
print date