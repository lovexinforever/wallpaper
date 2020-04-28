#!/usr/bin/env python
import sys
import datetime
import os
import io
sys.path.append('/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin')
from wand.image import Image as ImageWand
from wand.color import Color
from wand.drawing import Drawing
import cv2
import numpy as np

def compute(path):
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    img = cv2.imread(path, 1)
    per_image_Bmean.append(np.mean(img[:,:,0]))
    per_image_Gmean.append(np.mean(img[:,:,1]))
    per_image_Rmean.append(np.mean(img[:,:,2]))
    R_mean = np.mean(per_image_Rmean)
    G_mean = np.mean(per_image_Gmean)
    B_mean = np.mean(per_image_Bmean)
    return R_mean, G_mean, B_mean

if __name__ == "__main__":
    path = os.getcwd()  # now path
    pic_path = path + "/bin/weather/temp4.jpg"
    img = cv2.imread(pic_path)
    # cropped = img[470:510, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[470:510, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[470:510, 700:900]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[470:510, 1000:1200]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[510:550, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[510:550, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[510:550, 700:900]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[550:590, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[550:590, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[550:590, 700:900]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[670:710, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped = img[670:710, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped1 = img[50:150, 600:800]  # 裁剪坐标为[y0:y1, x0:x1]
    cropped1 = img[330:430, 100:800]  # 裁剪坐标为[y0:y1, x0:x1]
    # cropped2 = img[190:310, 600:2000]
    cv2.imwrite('cuts.jpg', cropped1)
    pic_path = path + "/cuts.jpg"
    R, G, B = compute(pic_path)
    Gray = R*0.299 + G*0.587 + B*0.114
    print(Gray)
    # print(path)
