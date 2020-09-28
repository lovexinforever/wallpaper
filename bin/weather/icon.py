#!/usr/bin/env python
# coding: utf-8
import json
import sys

def queryIcon(key):
    f = open("/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin/weather/icon.json",encoding='utf-8')
    origin = json.load(f);
    if(key in origin):
        # 获取 icon url
        icon = origin[key];
    # 如果获取不到,直接给默认
    else:
        icon = "http://img1.dianzedushu.cn/20101027235020136.png"

    print(icon)
    return icon;
