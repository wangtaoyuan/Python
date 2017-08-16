# encoding:utf-8
'''
Created on 2017年8月14日
题目：求1+2!+3!+...+20!的和。
@author: wangtaoyuan
'''
n = 20
result = 0
def jiecheng(x):#递归阶乘
    if x == 1:
        return 1
    else:
        return x * jiecheng(x - 1)
        
for i in range(1, n + 1):
    result += jiecheng(i)
print result