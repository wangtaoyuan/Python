# encoding:utf-8
'''
Created on 2017年8月4日
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

@author: wangtaoyuan
'''
print "请输入三个整数"
x = input('第一个数：')
y = input('第二个数：')
z = input('第三个数：')
if y < x:
    t = x
    x = y
    y = t
if z < x:
    t = x
    x = z
    z = t
if z < y:
    t = y
    y = z
    z = t
print x, y, z
    