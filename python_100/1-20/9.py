# encoding:utf-8
'''
Created on 2017年8月7日
题目：暂停一秒输出。
只是链接:
    1、time模块 的sleep()
    2、dict.items()
@author: wangtaoyuan
'''
import time
score = {'wang':100,'du':100,'tao':100}
for key,value in dict.items(score):
    print key, value
    time.sleep(1)
print dict.items(score)