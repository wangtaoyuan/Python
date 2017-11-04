# encoding:utf-8
'''
Created on 2017年8月18日
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
@author: wangtaoyuan
'''
list1 = [1, 3, 15, 37, 89, 256]
def panduan(list1):
    if list1[0] - list1[len(list1) - 1] > 0:#降序,比较首尾是担心相邻的数字相等
        return True
    else:#升序或者内部数字一样大
        return False

flag = panduan(list1)
list1.append(input('请输入要插入的数字：'))
list1.sort(reverse=flag)
print list1