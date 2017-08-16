# encoding:utf-8
'''
Created on 2017年8月14日
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
@author: wangtaoyuan
'''
num = input('请输入一个五位数')
strnum = str(num)
for i in range(len(strnum) / 2):  
    if strnum[i] == strnum[-1 - i]:
        if i == len(strnum) / 2 - 1:
            print '%d是一个回文数字' % num
    else:
        print '%d不是一个回文数字' % num
        break
