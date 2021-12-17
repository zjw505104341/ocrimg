# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/17 19:22
import cv2
import numpy as np
from PIL import Image

#创建回调函数
def OnMouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:  # 鼠标点击事件
        print({"x":x,"y":y})
        cv2.circle(img, (x, y), 15, (0, 0, 255), 1)

img = np.array(Image.open(r'C:\Users\50510\PycharmProjects\20210524\test\xinyongzhongguo\huakuai\originalImage.png'))
cv2.namedWindow('image')
cv2.setMouseCallback('image', OnMouse)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
cv2.destroyAllWindows()
