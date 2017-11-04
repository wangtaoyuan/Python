# encoding:utf-8
'''
Created on 2017年8月18日
题目：对10个数进行排序。
@author: wangtaoyuan
'''
import re
str = raw_input('请输入若干数字，中间用逗号分割')
num  = []
x = re.finditer(r'\d+',str)
for i in x:
    num.append(int(i.group()))
f = raw_input('升序输入s,降序输入j。请输入：')
if f == 'j':
    print sorted(num, reverse=True)
else:
    print sorted(num)
