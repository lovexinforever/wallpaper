#!/usr/bin/env python
# coding: utf-8
import json
import sys

def queryCode(key):
    f = open("/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin/weather/city.json", encoding='utf-8')
    origin = json.load(f);
    if(key in origin):
        # 获取城市编码
        code = origin[key];
    # 如果城市编码为空, 默认给南京编码
    else:
        code = "5ef652409badc75c97292b401c6db8e8e55a3157f300dc0997bea96343e4a20a"
    return code;