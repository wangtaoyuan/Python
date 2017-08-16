# encoding:utf-8
'''
Created on 2017年8月4日
题目：一个整数，它加上100后是一个完全平方数，加上268又是一个完全平方数，
请问该数是多少？
只是链接：开方
        import math
        math.sqrt()
@author: wangtaoyuan
'''
import math
i = [''] * 50
x = -100 #应该从负100开始，以为 -100加上100才为0，即查找完全平方数从0开始
j = 0
while  x < 10000:
    if math.sqrt(x + 100) % 1 == 0 and math.sqrt(x + 268) % 1 == 0:
        i[j] = x
        print i[j]
        j = j + 1      
    x = x + 1
