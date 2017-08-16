# encoding:utf-8
'''
Created on 2017年8月13日
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
@author: wangtaoyuan
'''
namelists = []
a = ('a', 'b', 'c')
b = ['x', 'y', 'z']
def luanxu(b2):
    t = b2[0]
    b2[0] = b2[1]
    b2[1] = b2[2]
    b2[2] = t
    return b2
def panduan(namelist_p):
    if namelist_p['a'] != 'x' and namelist_p['c'] != 'x' and namelist_p['c'] != 'z':
        return True
    else:
        return False
def zudui(a1, b1):
    global namelists
    for i in range(len(b1)):
        b1 = luanxu(b1)
        namelist = {}
        i = 0
        for i in range(len(a1)):
            namelist[a1[i]] = b1[i]
        if panduan(namelist):
            namelists.append(namelist)
zudui(a, b)
print namelists
for x in namelists:
    for key in x:
        print key, 'VS', x[key]
            
            
            
            
            
            
            