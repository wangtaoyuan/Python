# encoding:utf-8
'''
Created on 2017年8月12日
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
@author: wangtaoyuan
'''
wanshu = []
n = 1000
i = 0
j = 0
for i in range(1000):
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += j
            if count == i:
                wanshu.append(i)
                break
print wanshu