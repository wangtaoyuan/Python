# encoding:utf-8
'''
Created on 2017年8月4日
【程序4】
题目：输入某年某月某日，判断这一天是这一年的第几天？

@author: wangtaoyuan
'''
import re

date = raw_input("请输入年月日（例如 ：2017.8.4或者2017年8月4日）")
j = 0
for i in re.finditer(r'\d+', date):
    j += 1
    if j == 1:
        year = int(i.group())
    elif j ==2:
        month = int(i.group())
    else :
        day = int(i.group())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
rank = day
i = 0
while i < month - 1:
    rank = rank + months[i]
    i += 1
if year % 4 == 0 and month >= 3:
    if year % 100 != 0:
        rank = rank + 1
    else:
        if year % 400 == 0:
            rank = rank + 1
print year,'年',month,'月',day,'日','是当年的第',rank,'天'


    
