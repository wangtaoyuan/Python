# encoding:utf-8
'''
Created on 2017年8月11日
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
知识链接：
    1、一个中文字符在python中utf-8编码下占3个字节长度；unicode编码下则占1个字符
    2、str = str.decode('utf-8') 解码为unicode格式
@author: wangtaoyuan
'''
import re
'''错误原因：因为中文字符占用长度不是1，用len（）方法无法识别中文个数

str = raw_input('请输入一行字符')
words = re.findall(r'\w', str)
num = re.findall(r'\d', str)
space = re.findall(r' ', str)
print '字母个数为：', len(words) - len(num)
print '数字个数为：', len(num)
print '空格个数为：', len(space)
print '其他字符个数：', len(str) - len(words) - len(space)'''

#答案方法
str = raw_input('请输入一行字符：')
str = str.decode('utf-8')#解码成unicode类型,在unicode类型中，汉字占一位
word = 0
num = 0
space = 0
other = 0
for i in str:
    if re.match(r'\d', i):
        num += 1
    elif re.match(r'\w', i) and not re.match(r'\d', i):
        word += 1
    elif re.match(' ', i):
        space += 1
    else:
        other += 1
print '字母个数为：', word
print '数字个数为：', num
print '空格个数为：', space
print '其他字符个数：', other