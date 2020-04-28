#!/usr/bin/env python
#-*- coding: UTF-8 -*-  
import sys
import os
sys.path.append('/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin')
from weather import address
from weather import city
from weather import fiveday
if __name__ == '__main__':
    print(fiveday.getFives())
