#!/usr/bin/env python
import sys
import datetime
import os
import io
sys.path.append('/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin')
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from weather import fiveday
from PyPDF2 import PdfFileReader, PdfFileWriter
import cv2
import numpy as np

memo = {}
 
def getPdfReader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=False)
        memo[filename] = reader
    return reader


def composite_image(week_num, pdf_path, pic_path, pic_save_path):
    start_page = 7  # PDF start page
    dis_left = 1400
    dis_top = 10

    page = start_page + week_num

    pdfile = getPdfReader(pdf_path)
    pageObj = pdfile.getPage(page)
    dst_pdf = PdfFileWriter()
    dst_pdf.addPage(pageObj)

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)
    
    #with Image(filename=pdf_path.format(page), resolution=200) as calendar:
    with Image(file=pdf_bytes, resolution=200) as calendar:
        calendar.format = 'jpg'
        # calendar.background_color = Color("transparent")
        # with Color('#FFFFFF') as white:
        #     twenty_percent = int(65535 * 0.5)  # Note: percent must be calculated from Quantum
        #     calendar.transparent_color(white, alpha=0.0, fuzz=twenty_percent)
        with Image(filename=pic_path) as background:
            # background.composite_channel(
            #     'default_channels', calendar, 'blend', dis_left, dis_top)
            background.save(filename=pic_save_path)


def main():
    path = os.getcwd()  # now path
    #pdf_path = path + '/source/2018_code_calendar.pdf[{}]'  # pdf path
#    pdf_path = path + '/source/2019_code_calendar.pdf'  # pdf path
    pic_path = path + '/background/yosemiteonfire_2560x1440.jpg'  # wallpaper
    if len(sys.argv) > 1:
        pic_path = sys.argv[1]
    week_num = datetime.datetime.now().isocalendar()[1]
    if len(sys.argv) > 2:
        week_num = int(sys.argv[2])
    week_num_str = '0' + str(week_num) if week_num < 10 else str(week_num)

    pic_save_path = path + '/composite/code_calendar_wallpaper_' + week_num_str + '.jpg'  # new wallpaper

    composite_image(week_num, pdf_path, pic_path, pic_save_path)

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

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

def toHex(tmp):
    rgb = tmp.split(",")
    strs = "#"
    for j in range (0, len(rgb)):
        num = int(rgb[j])
        strs += str(hex(num))[-2:]
    return strs
def toNewColor(R, G, B):
    newR = int((255-R))
    newG = int((255-G))
    newB = int((255-B))
    newRgb = str(newG) + "," + str(newG) + "," + str(newB)
    return newRgb

def create_image_search(image_name, fives, save_path, parent_path):
    five = fives['fiveWeather']
    """Create an image with the given string"""
    with Image(filename=image_name) as img:
        img.blur(img.width/2, 10)
        with img.clone() as cloned:
            cloned.format = 'png'
            with Drawing() as draw:
                cvImage = cv2.imread(image_name)
                draw.font='/Users/dingyang/tim/extra/my/wall/Mac-command-wallpaper-master/bin/weather/font/WawaSC-Regular.otf'
                draw.font_size = 30
                # 星期
                cropped = cvImage[470:510, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(100, 500, five[1]['week'])

                cropped = cvImage[470:510, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(400, 500, five[2]['week'])

                cropped = cvImage[470:510, 700:900]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(700, 500, five[3]['week'])

                cropped = cvImage[470:510, 1000:1200]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(1000, 500, five[4]['week'])
                
                draw.font_size = 25
                # 日期
                cropped = cvImage[510:550, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(100, 540, five[1]['date'])

                cropped = cvImage[510:550, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(400, 540, five[2]['date'])
                cropped = cvImage[510:550, 700:1000]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(700, 540, five[3]['date'])
                cropped = cvImage[510:550, 1000:1200]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(1000, 540, five[4]['date'])

                # 天气
                cropped = cvImage[550:590, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(100, 580, five[1]['des'])
                cropped = cvImage[550:590, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(400, 580, five[2]['des'])
                cropped = cvImage[550:590, 700:1000]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(700, 580, five[3]['des'])
                cropped = cvImage[550:590, 1000:1200]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(1000, 580, five[4]['des'])

                # 温度
                cropped = cvImage[670:710, 100:300]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(100, 700, five[1]['temp'])
                cropped = cvImage[670:710, 400:600]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(400, 700, five[2]['temp'])
                cropped = cvImage[670:710, 700:1000]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(700, 700, five[3]['temp'])
                cropped = cvImage[670:710, 1000:1200]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(1000, 700, five[4]['temp'])
                
                with Image(filename='/tmp/weather.png') as oneday:
                    draw.composite(operator = 'atop',
                        left = 200, top = 150,
                        width = 350,
                        height = 350 * oneday.height / oneday.width,
                        image = oneday)

                with Image(filename='/tmp/five1.png') as twoday:
                    draw.composite(operator = 'atop',
                        left = 110, top = 610,
                        width = 80,
                        height = 80 * twoday.height / twoday.width,
                        image = twoday)
                with Image(filename='/tmp/five2.png') as threeday:
                    draw.composite(operator = 'atop',
                        left = 410, top = 610,
                        width = 80,
                        height = 80 * threeday.height / threeday.width,
                        image = threeday)
                with Image(filename='/tmp/five3.png') as fourday:
                    draw.composite(operator = 'atop',
                        left = 710, top = 610,
                        width = 80,
                        height = 80 * fourday.height / fourday.width,
                        image = fourday)
                with Image(filename='/tmp/five4.png') as fiveday:
                    draw.composite(operator = 'atop',
                        left = 1010, top = 610,
                        width = 80,
                        height = 80 * fiveday.height / fiveday.width,
                        image = fiveday)

                draw.font_size = 80
                
                cropped = cvImage[50:150, 600:800]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(600, 120, five[0]['temp'])
                cropped = cvImage[330:430, 100:800]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(600, 120, five[0]['temp'])
                draw.text(130, 400, five[0]['des'])
                
                draw.font_size = 160
                cropped = cvImage[190:310, 600:2000]  # 裁剪坐标为[y0:y1, x0:x1]
                cv2.imwrite('cut.jpg', cropped)
                pic_path = os.getcwd() + "/cut.jpg"
                R, G, B = compute(pic_path)
                newRgb = toNewColor(R, G, B)
                draw.stroke_color=Color(toHex(newRgb))
                draw.fill_color=Color(toHex(newRgb))
                draw.text(630, 300, fives['addr'])
                draw(cloned)
                del_file(parent_path+'/composite')
                del_file(parent_path+'/background')
                cloned.save(filename=save_path)
                # img = cv2.imread(save_path)
                # cropped = img[480:510, 100:200]  # 裁剪坐标为[y0:y1, x0:x1]
                # cv2.imwrite('cut.jpg', cropped)
                os.system("echo pic complete >> /tmp/service.txt")


if __name__ == "__main__":
    # main()
    os.system('echo "get weather start" >> /tmp/service.txt')
    fives = fiveday.getFives()
    path = os.getcwd()  # now path
    #pdf_path = path + '/source/2018_code_calendar.pdf[{}]'  # pdf path
    pdf_path = path + '/source/2019_code_calendar.pdf'  # pdf path
    pic_path = path + '/background/yosemiteonfire_2560x1440.jpg'  # wallpaper
    if len(sys.argv) > 1:
        pic_path = sys.argv[1]
    if len(sys.argv) > 2:
        date = sys.argv[2]

    pic_save_path = path + '/composite/code_calendar_wallpaper_' + str(date) + '.jpg'  # new wallpaper
    create_image_search(pic_path,fives, pic_save_path, path)

