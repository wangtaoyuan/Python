# encoding:utf-8
'''
Created on 2017年8月15日
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
@author: wangtaoyuan
'''
#Sunday Monday Tuesday wednesday Thursday Friday Saturday
weeks = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
j = 1
str = raw_input('请输入第%d字母' % j )
def judgeday(str,  maybe = []):
    maybe2 = []#用来装在本次判断中可能的答案，maybe[]用来接收上一次判断中可能的答案
    if len(maybe) == 0:
        for x in weeks:
            for i in range(len(x)):
                if str.lower() == x[i]:
                    maybe2.append(x)
    else:       
        for x in maybe:
            for i in range(len(x)):
                if str.lower() == x[i]:
                    maybe2.append(x)
                    
    if len(maybe2) == 1:#第一个输出点
        return maybe2[0]
    elif len(maybe2) > 1:
        global j
        j = j + 1
        str = raw_input('无法确定请再输入第%d个字母' % j)
        return judgeday(str, maybe2)  #第二个输出点，如果递归到第二层第一个的输出只能return到第一层的这个地方，并不能退出所有递归
weekd = judgeday(str)
if weekd is None:
    print '不存在'
else:
    print 'The day is', weekd