# encoding:utf-8
'''
Created on 2017年10月10日
题目：学习使用auto定义变量的用法
@author: wangtaoyuan
'''
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1#因为在函数autofun()中的num为局部变量，所以，num永远=1,num+=1也失效
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()