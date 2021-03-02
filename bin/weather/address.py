#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import sys
import os
import importlib
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
importlib.reload(sys)
import time

def queryIpAddress(ipaddress):
    chrome_options=Options()
    #设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    url='http://ip.tool.chinaz.com/'+ipaddress
    print(url)
    
    browser.get(url)
    #    head={}
    #    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    #    req=request.Request(url,headers=head)
    #    reaponse = request.urlopen(req);
    soup=BeautifulSoup(browser.page_source,'html.parser');
    a = soup.find('div', attrs={'class': 'WhoIpWrap'})
#    print(a);
    b = a.find_all('p')[0].get_text();
    # print(b)
    address = b.split(' ')[0]
    return address

def get_ip():
    url='http://ip.42.pl/raw'
    head={}
    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    req=request.Request(url,headers=head)
    ip = request.urlopen(req).read().decode('utf-8');
    print(ip)
    os.system('echo "get ip success" >> /tmp/service.txt')
    return ip
