from urllib import request
from urllib.parse import quote
import string
import os
import json
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

def getCal(year, month):
    path = 'bin/weather/'+year+'-'+month+'.json'
    jsons = ''
    if os.path.exists(path):
        f = open(path, encoding='utf-8')
        jsons = json.load(f);
    else:
        url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query='+year+'年'+month+'月&resource_id=6018&format=json'
        url = quote(url,safe=string.printable)
        head={}
        print(url)
        head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        req=request.Request(url,headers=head)
        jsons = request.urlopen(req).read().decode('gbk');
        try:
            f = open(path, 'w');
            f.write(jsons)
        finally:
            f.close()
    return jsons
def drawPic(image_name, save_path):
    with Image(filename=image_name) as img:
        img.blur(img.width/2, 10)
        with img.clone() as cloned:
            cloned.format = 'png'
            with Drawing() as draw:

                
                
                draw.stroke_dash_array=[100, 200]
                draw.stroke_dash_offset=200
                draw(cloned)
                cloned.save(filename=save_path)

if __name__ == '__main__':
    # print(getCal('2019', '1'))
    # drawPic('bin/weather/temp.jpg','bin/weather/final.jpg')