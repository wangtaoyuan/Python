# encoding:utf-8
'''
Created on 2017年8月16日
题目：练习函数调用。
知识链接:
    1、__name__ = '__main__'
    2、函数可以定义参数默认值，若不传入参数则为默认值
@author: wangtaoyuan
'''

def jia1(*args):
    result = 0
    for x in args:
        result += x
    print result, '1'
def jia(a, b = 3):
    print  a + b
if __name__ == '__main__':
     jia(1, 2)
     jia1(1, 2, 3, 4)
     jia(1)