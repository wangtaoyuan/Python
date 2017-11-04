# encoding:utf-8
'''
Created on 2017年8月18日

@author: wangtaoyuan
'''
n = 100
def sushu(n):
    for i in range(1, n):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            print i
sushu(n)