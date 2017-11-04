# encoding:utf-8
'''
Created on 2017年11月2日
题目：两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
@author: wangtaoyuan
'''
x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
result = [[], [], []]
for i in range(3):
    for j in range(3):
        #result[i][j] = x[i][j] + y[i][j]
        #不可另result直接 等，是因为定义的result并未开闭相应空间。应用append()或者定义result为result[[0,0,0],[0,0,0],[0,0,0]]
        result[i].append(x[i][j] + y[i][j]) 
print result   
    