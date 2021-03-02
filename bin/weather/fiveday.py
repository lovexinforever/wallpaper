#!/usr/bin/env python
# encoding=utf8
import sys
sys.path.append('/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin')
from weather import address
import importlib
from weather import city
from weather import icon
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import socket
socket.setdefaulttimeout(300)
from bs4 import BeautifulSoup
importlib.reload(sys)
import re

def getFives():
    five = getToday()
    fiveWeather = five['fiveWeather']
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    chrome_options=Options()
    #设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    url = "https://weather.com/zh-CN/weather/tenday/l/"+code
    browser.get(url)
    
    soupFive=BeautifulSoup(browser.page_source,'html.parser');
    
    # 最近五天
    main=soupFive.select('main[id="MainContent"]')
    # print(main)
    # print(soupFive.select('section')[0])
    fives=main[0].select('section')[0].find_all('details');
    # print(fives)
    for index in range(len(fives)):
        if(index != 0):
            # 天气描述
            # print(fives[index])
            currentDesTag = fives[index].find('div',attrs={'data-testid':'wxIcon'}).find('span');
            # print(currentDesTag)
            # 日期所处的位置
            # week=fives[index].find_all('td',attrs={'class':'twc-sticky-col'})[1];
            week = fives[index].find("h2", attrs={'data-testid': "daypartName"}).get_text()
            # print(week)
            # 日期
            weekDate=week.split(' ')[1];
            weekContent=week.split(' ')[0];
            # print(weekDate)
            # 温度
            currentTempTag=fives[index].find('div',attrs={'data-testid':'detailsTemperature'}).find_all('span');
            currentTemp = currentTempTag[0].get_text()+" / "+currentTempTag[2].get_text()
            # print(currentTemp)
            # 图标存储路径
            iconpath = '/tmp/five' + str(index) + '.png'
            currentDes = currentDesTag.get_text()
            # weekDate = weekDate.get_text()
            # weekContent = weekContent.get_text()
            current = {}
            current['des'] = currentDes
            current['date'] = weekDate
            current['week'] = weekContent
            current['temp'] = currentTemp
            fiveWeather.append(current)
            #解决下载不完全问题且避免陷入死循环
            try:
                request.urlretrieve(icon.queryIcon(currentDes), iconpath)
            except socket.timeout:
                count = 1
                while count <= 5:
                    try:
                        request.urlretrieve(icon.queryIcon(currentDes), iconpath)
                        break
                    except socket.timeout:
                        count += 1
                if count > 5:
                    print("downloading picture fialed!")
    return five;

def getToday():
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    fives = {}
    fiveWeather = []
    code = city.queryCode(addr)
    chrome_options=Options()
    #设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    url = "https://weather.com/zh-CN/weather/today/l/"+code
    print(url)
    browser.get(url)
    soup=BeautifulSoup(browser.page_source,'html.parser');
    # print(soup)
    tagTodayTemp=soup.find('span',attrs={'data-testid':'TemperatureValue'})
    tagTodayDes=soup.find('div',attrs={'data-testid':'wxPhrase'})
    # print(tagTodayDes)
    # print(tagTodayTemp)
    request.urlretrieve(icon.queryIcon(tagTodayDes.get_text()), '/tmp/weather.png')
    current = {}
    current['des'] = tagTodayDes.get_text()
    current['temp'] = tagTodayTemp.get_text()
    fiveWeather.append(current)
    fives['addr'] = addr
    fives['fiveWeather'] = fiveWeather
    
    return fives

