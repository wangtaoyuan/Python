# encoding:utf-8
'''
Created on 2017年8月5日
题目：斐波那契数列

知识链接：
    递归调用的自我理解：从通式入手，代码内容内部回溯到最底层即最开始

        

@author: wangtaoyuan
'''
# x = input("查找第几个斐波那契数列的数字")

x = 1
while x < 13:
    def Fib(x):
        if x == 1:
            return 0
        elif x == 2:
            return 1
        else:
            return Fib(x - 1) + Fib(x -2)
    print Fib(x) 
    x += 1     
