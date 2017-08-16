# encoding:utf-8
'''
Created on 2017年8月3日

@author: wangtaoyuan
'''
import urllib
#<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>
str0 = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'

title = str0.find(r'<a title')
href = str0.find(r'href=')
print href
html = str0.find(r'.html')
print html
url = str0[href + 6:html + 5]
print url
content = urllib.urlopen(url).read()#将网页内容读取下来
filename = url[-26:]
open(filename, 'w').write(content)

