# encoding:utf-8
'''
Created on 2017年8月14日
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
知识链接：
    1、输入数字前加0时，默认为8进制
    2、print 后字符串中有多个参数时，%后的变量要用()括起来
@author: wangtaoyuan
'''
num = input('请输入一个不多于5位的正整数')
l = len(str(num))
print '%d是个%d位数' % (num, l)
for i in range(l):
    print num % 10,
    num = (num - num % 10) / 10
