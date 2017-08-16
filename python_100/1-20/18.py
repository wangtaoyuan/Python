# encoding:utf-8
'''
Created on 2017年8月11日
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
@author: wangtaoyuan
'''
n = input('请输入几个数相加：')
a = raw_input('请输入要a数字：')
def createnum(n, a):
    num = []
    for i in range(n):
        num.append(int(a * (i + 1)))
    return num
def addnum(n, num):
    sum = 0
    print 'sum=',
    for i in range(n):
        sum = sum + num[i]
        if i == n - 1:
            print num[i],
        else:
            print num[i], '+',
    print '=', sum
num = createnum(n, a)
addnum(n, num)
