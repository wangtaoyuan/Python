# encoding:utf-8
'''
Created on 2017年8月5日

@author: wangtaoyuan
'''
import urllib2
import os
import time
#http://www.runoob.com/python/python-exercise-example1.html
i = 1
# if os.path.isdir('..\exercise100') == False :
#     os.makedirs('..\exercise100')
while i < 101:
    url = 'http://www.runoob.com/python/python-exercise-example' + '%d' % i + '.html'
    print url
    content = urllib2.urlopen(url).read()
    head = content.find(r'<p><strong>题目：</strong>') + len('<p><strong>题目：</strong>')
    tail = content.find(r'</p>', head)
    if head < tail and head != 28 and tail != -1:
        article = content[head: tail]
        print '第%d题 : ' % i
        if i == 1:
            open(r'exercise100\100.txt','w').write('题目 %d：' % i+ article + '\n\n')
        else:
            open(r'exercise100\100.txt','a').write('题目 %d：' % i+ article + '\n\n') 
    else:
        print '第%d个题目爬取失败' % i
        if i == 1:
            open(r'exercise100\100.txt','w').write('题目 %d：' % i + '爬取失败' + ',题目网址是：%s' % url +'\n\n')
        else:
            open(r'exercise100\100.txt','a').write('题目 %d：' % i + '爬取失败' + ',题目网址是：%s' % url + '\n\n')
    i = i + 1

    print head, tail

  
# print 'reading exercise 1...'
# open(r'exercise100/%d' % i  + '.html', 'w').write(content)
# time.sleep(1)
# print 'downloaded complete.'

