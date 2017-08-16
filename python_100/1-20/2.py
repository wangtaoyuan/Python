# encoding:utf-8
'''
Created on 2017年8月3日
简述：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
           利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
      20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
            可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成.
提问：从键盘输入当月利润I，求应发放奖金总数？
@author: wangtaoyuan
'''
profit = input("请输入当月利润(单位：万元)：")

def bonus0(profit):
    b0 = profit * 0.1
    return b0

def bonus10(profit):
    b1 = (profit - 10) * 0.075 + bonus0(10)
    return b1


def bonus20(profit):
    b2 = (profit - 20) * 0.05 + bonus10(20)
    return b2

def bonus40(profit):
    b4 = (profit - 40) * 0.03 + bonus20(40)
    return b4

def bonus60(profit):
    b6 = (profit - 60) * 0.015 + bonus40(60)
    return b6

def bonus100(profit):
    b10 = (profit - 100) * 0.001 + bonus60(100)
    return b10

if profit > 100:
    b = bonus100(profit)
elif 60 < profit  <= 100:
    b = bonus60(profit)
elif 40 < profit <= 60:
    b = bonus40(profit)
elif 20 < profit <= 40:
    b = bonus20(profit)
elif 10 < profit <= 20:
    b = bonus10(profit)
else:
    b = bonus0(profit)  
    
print '当月奖金：', b,"万元"