# encoding:utf-8
'''
Created on 2017年8月6日
题目：输出 9*9 乘法口诀表。
知识链接：
    1、print不换行:
        python 2.0+：    print 'a',
        python 3.0+    print ('a', end="")
    2、print中，避免逗号引起的空格（比如print 1,2）
        print "%d%d" % (a,b)
@author: wangtaoyuan
'''
for i in range(1,10):
    for j in range(1,i + 1):
        print '%d*%d=%d   ' % (j, i, (i * j)),
    print '\n'