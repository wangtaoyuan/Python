# encoding:utf-8
'''
Created on 2017年8月3日
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
@author: 84629
'''
sor = [1, 2, 3 ,4]
count = 0 
for g in sor:
    for s in sor:
        for b in sor:
            if g != s and g != b  and s != b :
                print g + s * 10 + b * 100 
                count = count + 1
print "总共有%d个这样的数字" % count    