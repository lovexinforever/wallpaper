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

def queryCal():
    chrome_options=Options()
    #设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    url='http://yun.rili.cn/wnl/index.html'
    print(url)
    
    browser.get(url)
    time.sleep(3)
    #    head={}
    #    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    #    req=request.Request(url,headers=head)
    #    reaponse = request.urlopen(req);
    soup=BeautifulSoup(browser.page_source,'html.parser');
    a = soup.find('table', attrs={'id': 'cont'}).find_all('td')
    # print(a)
    print(len(a))
    # b = soup.find('td', attrs={'class': 'today'}).parent();
    # print(len(b))
    calList = []
    for index in range(len(a)):
        current = {};
        current['number'] = a[index].find('div', attrs={'class': 'number'}).text
        current['lnumber'] = a[index].find('div', attrs={'class': 'lnumber'}).text
        if a[index].find('div', attrs={'class': 'jprestWork'}) == None:
            current['type'] = 0 # 正常
        else:
            if a[index].find('div', attrs={'class': 'jprestWorkw'}) == None:
                current['type'] = 1 # 假期
            else:
                current['type'] = 2 # 班

        calList.append(current)
        # print(a[index].find('div', attrs={'class': 'number'}))
        # print(a[index].find('div', attrs={'class': 'number'}).text)
        # print(a[index].find('div', attrs={'class': 'lnumber'}))
        # print(a[index].find('div', attrs={'class': 'jprestWork'}) == None)
        # print(a[index].find('div', attrs={'class': 'jprestWorkw'}) == None)
    
    # b = a.find_all('p')[1].find_all('span')[3].get_text();
    # # print(b)
    # address = b.split(' ')[0]
    return calList

if __name__ == "__main__":
    print(queryCal())

