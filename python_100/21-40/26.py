# encoding:utf-8
'''
Created on 2017年8月14日
题目：利用递归方法求5!。
@author: wangtaoyuan
'''
x = input('请输入要求阶乘的整数')
def jiecheng(x):
    if x == 1:
        return 1
    elif x <= 0 or x % 1 != 0:
        return 
    else:
        return x * jiecheng(x - 1)
print jiecheng(x)