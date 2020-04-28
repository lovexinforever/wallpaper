#!/usr/local/bin/python3.6
import os
import time

def wallpaper():
    while  True:
        os.system('echo "getwallpaper" >> /tmp/service.txt')
        os.system('./wallpaper randweb com')
        time.sleep(60 * 1)


if __name__ == "__main__":
        os.system('echo "wallpaper.py" >> /tmp/service.txt')
        wallpaper()