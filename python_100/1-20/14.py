# encoding:utf-8
'''
Created on 2017年8月8日
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
@author: wangtaoyuan
'''
zs = []
zsfj = []
x = input('请输入一个数字：')
x1 = x

def zhishu(x):
    global zs
    for i1 in range(1, x):
        count = 0
        for i2 in range(1, i1):
            if i1 % i2 == 0:
                count += 1
#                 zsfj.append(i2)
        if count == 1:
            zs.append(i1)
def fenjie(x1):  
    def chu(ia):
        global x1
        if x1 % ia == 0:
            x1 = x1 / ia
            zsfj.append(ia)
            return True
        else:
            return False
    global zs
    for ia in zs:
        while True:
            flag = chu(ia)
            if flag == False:
                break
def output():
    global zs, zsfj, x
    i = 0
    print x, '=',
    for i in range(0, len(zsfj)):
        if i != (len(zsfj) - 1):
            print  zsfj[i], '*',
        else:
            print zsfj[i]
zhishu(x)
fenjie(x)
output()