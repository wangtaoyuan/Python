# encoding:utf-8
'''
Created on 2017年8月15日
题目：按逗号分隔列表。
知识链接：
    1、''.join()函数，连接字符串
@author: wangtaoyuan
'''
L = [1, 2, 3, 4, 5, 6]
s1 = ','.join(str(n) for n in L)
print s1