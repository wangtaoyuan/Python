# encoding:utf-8
'''
Created on 2017年8月16日
1、审查元素中查找backgroudimage
@author: wangtaoyuan
'''
import urllib2
import requests
import time

url = 'http://cn.bing.com'
#伪装头信息
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,headers)

content = urllib2.urlopen(url).read()
head = content.find(r'g_img=') + len(r'g_img={url: "')
tail = content.find(r'.jpg') + 4
img_url = url + content[head: tail]#对content进行切片取图片的url
time.sleep(1)
print img_url

def downloadpic(image_url, save_path):
    r = requests.get(image_url)

    with open(save_path, "wb") as code:
        code.write(r.content)
tday = time.strftime('%Y%m%d',time.localtime()) 
print tday    
save_path = 'E:\\background\\bing%s.jpg' % tday
downloadpic(img_url, save_path)
