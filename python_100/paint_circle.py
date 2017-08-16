# encoding:utf-8
'''
Created on 2017年8月5日
【程序6】
题目：用*号输出字母C的图案。
程序分析：

知识链接：
    取整：
    math.ceil()  向上取整
    math.floor() 向下取整
    round()      四舍五入
    取绝对值：
    abs()
        

@author: wangtaoyuan
'''
import math
R = 10
P = math.sqrt(R * R - (R / 2) * (R / 2))#（R-P）是c的上切口点的纵坐标
space =' '
row = 0
print space * (R/2), '*'


def paint(x):
    print ' ' * int(x), '*', ' ' * int(R - x)*2, '*'


while row < 2*R:
    y = row 
    dy = R - y
    dx = round(R * R - dy * dy)
    x = R - dx
    paint(x)
    row = row + 1
        
        
