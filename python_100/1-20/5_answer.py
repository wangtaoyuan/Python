# encoding:utf-8
'''
Created on 2017年8月4日
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
@author: wangtaoyuan
'''
a = [''] * 3
for i in range(3):
    a[i] = input('请输入第%d个数字:' % (i + 1))
a.sort()
print a