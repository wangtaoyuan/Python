# encoding:utf-8
'''
Created on 2017年8月12日
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，
当即吃了一半，还不瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
@author: wangtaoyuan
'''
n = 1
day = 10
def tutaozi(n1, day1):
    if day1 > 1:
        n1 = (n1 + 1) * 2 
        day1 -= 1
        tutaozi(n1, day1)
    else:
        print n1
tutaozi(n, day)