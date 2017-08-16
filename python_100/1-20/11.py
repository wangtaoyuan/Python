# encoding:utf-8
'''
Created on 2017年8月7日
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
知识链接：
    1、在使用函数传递变量时不要同全局变量的名称一样
    2、全局变量在函数中使用时，需要用 global声明
@author: wangtaoyuan
'''
new = 1#刚出生的小兔子对数
one = 0#一个月大的兔子对数
old = 0#两个月及以上的兔子，成熟兔子对数
i = 0
m = input('please input a inter of months:')
print '                                   ',old + new + one#初始兔子的总数
def growup( newl, onel, oldl):
    global new, old, one, two
    old = oldl + onel#1个月大的兔子成长为成熟兔子
    print 'old:',old
    one = newl #刚出生的兔子成长为一个月大的兔子
    print 'one:', one
    new = 0 
def breed(oldl):
    global new
    new = old #一对成熟兔子可以下一对刚出生的小兔子
    print 'new:', new
while i < m:
    print i+1,'个月后：' 
    growup(new, one, old)#成长1个月
    breed(old)#成熟的兔子生小兔子
    i += 1
    
    print '                                   ',old + new + one#兔子的总数
