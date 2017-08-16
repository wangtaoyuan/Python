# encoding:utf-8
'''
Created on 2017年8月12日
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
@author: wangtaoyuan
'''
height = 100.0
n = 10
through = 0
def fantan(n1, height1):
    global  through
    through =through + height1 + height1 / 2
    if n1 > 1:
        fantan(n1 - 1, height1 / 2)
    else :
        print through, height1 / 2    
fantan(n, height)