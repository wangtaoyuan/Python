# encoding:utf-8
'''
Created on 2017年8月8日
题目：判断101-200之间有多少个素数，并输出所有素数。
素数：只能被1或自身整除的数
@author: wangtaoyuan
'''
answer = [] 
a = 1
b = 201
for x in range(a, b):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count = count + 1
            i += 1
    if count == 1:
        answer.append(x)
    x += 1
totality = 0
for real in answer:
    totality += 1
    print real
print a, '到', b, '的素数总共有', totality, '个'