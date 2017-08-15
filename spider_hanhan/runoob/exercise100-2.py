# encoding:utf-8
'''
Created on 2017年8月11日

@author: wangtaoyuan
'''
import requests
from bs4 import BeautifulSoup
r = requests.get('http://202.206.217.109/')
print r.text
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p')
for item in pattern:
    print item.string