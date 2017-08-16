# encoding:utf-8
'''
Created on 2017年8月10日
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
@author: wangtaoyuan
'''
score = input('请输入成绩：')
if score >= 90:
    print 'A'
    if 60 <= score <= 89:
        print 'B'
        if score < 60:
            print 'C'
