# encoding:utf-8
'''
Created on 2017年8月13日
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
@author: wangtaoyuan
'''
result = 0
n = 20
def yuefen(m, z):
    i = 2
    while True:
        if m % i == 0 and z % i == 0:
            m = m / i
            z = z / i
        i += 1
        if i > m or i > z:
            break
    return m, z
def fenshuappend(am, az, bm, bz):
    m = am * bm
    z = az * bm + bz * am
#     m, z = yuefen(m, z)
    return m, z

i = 1
while i < n:
    if i == 1:
        a1 = 1
        a2 = 2
        b1 = a2
        b2 = a1 + a2
    print  b2,'/', b1
    m, z = fenshuappend(a1, a2, b1, b2)
    print m, z
    t = b1
    b1 = b2
    b2 = t + b2
    a1 = m
    a2 = z
    i += 1
print z, '/', m
print float(z)/m
    