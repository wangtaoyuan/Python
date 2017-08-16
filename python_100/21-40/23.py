# encoding:utf-8
'''
Created on 2017年8月13日
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
@author: wangtaoyuan
'''
def paintlx(l):
    for i in range(l / 2):
        print ' ' * (l / 2 - i) + '*' * (i * 2 + 1)
    print '*' * l
    for i in range(l / 2 - 1, -1, -1):
        print ' ' * (l / 2 - i) + '*' * (i * 2 + 1)
while True:
    l = raw_input('请输入菱形腰长(奇数)，默认为7：')
    if l == '':
        l = 7
        paintlx(int(l))
        break
    elif int(l) % 2 == 0:
        print '说了是奇数！'
    else:
        paintlx(int(l))
        break
        
