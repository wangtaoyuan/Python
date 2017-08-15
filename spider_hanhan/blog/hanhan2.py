# encoding:utf-8
'''
Created on 2017年8月3日

@author: wangtaoyuan
'''
import urllib
import time
#<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>

url = ['']*50
con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
title = con.find(r'<a title=')
href = con.find(r'href=', title)
html = con.find(r'.html', href)
i = 0
while title != -1 and href != -1 and html != -1 and i < 50 :  
    url[i] = con[href + 6:html + 5]
    print url[i]
    
    title = con.find(r'<a title=', html)
    href = con.find(r'href=', title)
    html = con.find(r'.html', href)
    i = i + 1
else:
    print 'find end!'
# print url[0]
print i
j = 0  
while j < 50:
    content = urllib.urlopen(url[j]).read()
    open(r'hanhan/'+url[j][-26:], 'w+').write(content)#将url的后26个字符作为文章名称 ;w+ ,加号表示在没有此文件夹时自动创建
    print 'downloading', url[j]
    j = j + 1
    time.sleep(2)
else:
    print 'download article finished'
    



