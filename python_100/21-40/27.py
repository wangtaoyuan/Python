# encoding:utf-8
'''
Created on 2017年8月14日
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
@author: wangtaoyuan
'''
str = raw_input('请输入').decode('utf-8')
def reoutput(str):
    if len(str) == 0:
        return
    print str[-1]
    str = str[0: len(str) - 1]
    reoutput(str)
reoutput(str)