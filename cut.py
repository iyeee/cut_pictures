# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
#指明被遍历的文件夹
rootdir = r'E:\Document\pictures\未命名 (1)\footage'
for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
   
        img = Image.open(currentPath)
        print (img.format, img.size, img.mode)
        #img.show()
        box1 = (17, 16, 158, 189)#设置左、上、右、下的像素
        image1 = img.crop(box1) # 图像裁剪
        image1.save(r"E:\AD datasets\voiceClassifyGoogle\Class\C_2"+'\\'+filename) #存储裁剪得到的图像