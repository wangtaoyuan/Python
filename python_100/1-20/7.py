# encoding:utf-8
'''
Created on 2017年8月6日
题目：将一个列表的数据复制到另一个列表中。
知识链接：
    a, b为列表时，    b = a 只是把a的地址赋给了b,a变化时，b也跟着变化。
    copy.copy()
    b = a[:]  ,切片[:]，表示a的全部内容，从0位到最后一位
@author: wangtaoyuan
'''
import copy
a = ['a', 'b', 'c']
b = copy.copy(a)
print b 

c = ['e', 'f', 'g']
d = c[:]
print d