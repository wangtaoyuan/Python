# encoding:utf-8
'''
Created on 2017年8月8日
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
@author: wangtaoyuan
'''
a = 100
b = 1000
count = 0
for x in range(a, b):
    ge = x % 10
    shi = x % 100 / 10
    bai = x / 100
    if (ge ** 3 + shi ** 3 + bai ** 3) == x:
        print x
        count += 1
print '总共有', count, '个水仙花数'