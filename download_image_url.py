#<Download Image Set>

import io  #https://docs.python.org/3.6/library/io.html
import os  #https://docs.python.org/3/library/os.html

from PIL import Image 
import requests        # pip install requests 
import time            #

dir_name = "catbox"
fo = open("catbox-synset.txt","r") # print("Image File Name:",fo.name)

# Make a New Directory 建立新資料夾
 if not os.path.exists(dir_name):    #先確認資料夾是否存在
    os.makedirs(dir_name)

#路徑
Path = ('C:/Users/yi-hua/Desktop/ImageNet/{}'.format(dir_name))

#Download Image Set
def download_image(url, image_file_path):
    r = requests.get(url, timeout=4.0)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)

    with Image.open(io.BytesIO(r.content)) as im:
        im.save(image_file_path)
    print('Image downloaded from url: {} and saved to: {}.'.format(url, image_file_path))


    

for idx, url in enumerate(fo.readlines()):
    
    image_file_path = ('{}/{}.jpg'.format(Path, idx))
    url = url.strip()
    
    #print("url: %s "% (url))
    try:
        download_image(url, image_file_path)
        time.sleep(1)          #sleep for 1 s
    except Exception as e:
        print(url)
        print(e)
fo.close()