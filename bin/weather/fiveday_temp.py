#!/usr/bin/env python
# encoding=utf8
import sys
sys.path.append('/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin')
from weather import address
from weather import city
from weather import icon
from urllib import request
import os
import socket
socket.setdefaulttimeout(30)
from bs4 import BeautifulSoup
import re

def getFives():
    five = getToday()
    fiveWeather = five['fiveWeather']
    addr = address.queryIpAddress(address.get_ip())
    code = city.queryCode(addr)
    url = "https://weather.com/zh-CN/weather/5day/l/"+code
    respFive=request.urlopen(url);
    soupFive=BeautifulSoup(respFive,'html.parser');
    
    # 最近五天
    fives=soupFive.find_all('tr',attrs={'class':'clickable'});
    for index in range(len(fives)):
        if(index != 0):
            # 天气描述
            currentDesTag = fives[index].find('td',attrs={'class':'description'});
            # 日期所处的位置
            week=fives[index].find_all('td',attrs={'class':'twc-sticky-col'})[1];
            # 日期
            weekDate=week.find('span',attrs={'class':'day-detail'});
            weekContent=week.find('span',attrs={'class':'date-time'});
            # 温度
            currentTempTag=fives[index].find('td',attrs={'class':'temp'}).find_all('span');
            currentTemp = currentTempTag[0].get_text()+" / "+currentTempTag[2].get_text()
            # 图标存储路径
            iconpath = '/tmp/five' + str(index) + '.png'
            currentDes = currentDesTag.get_text()
            weekDate = weekDate.get_text()
            weekContent = weekContent.get_text()
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
    url = "https://weather.com/zh-CN/weather/today/l/"+code
    respFive=request.urlopen(url);
    soup=BeautifulSoup(respFive,'html.parser');
    tagTodayTemp=soup.find('div',attrs={'class':'today_nowcard-temp'})
    tagTodayDes=soup.find('div',attrs={'class':'today_nowcard-phrase'})
    request.urlretrieve(icon.queryIcon(tagTodayDes.get_text()), '/tmp/weather.png')
    current = {}
    current['des'] = tagTodayDes.get_text()
    current['temp'] = tagTodayTemp.get_text()
    fiveWeather.append(current)
    fives['addr'] = addr
    fives['fiveWeather'] = fiveWeather
    return fives

