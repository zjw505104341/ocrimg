# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/17 16:03
import cv2, numpy


def get_w(small_img, big_img):
    small_img = numpy.frombuffer(small_img, dtype=numpy.uint8)
    big_img = numpy.frombuffer(big_img, dtype=numpy.uint8)
    small_img = cv2.imdecode(small_img, cv2.IMREAD_COLOR)
    big_img = cv2.imdecode(big_img, cv2.IMREAD_COLOR)
    # small_img = cv2.imread(small_img) # 小图
    # big_img = cv2.imread(big_img)  #　 大图
    
    gray = cv2.cvtColor(small_img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)   # 灰度
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 轮廓检测
    bottom = max([i[1] for i in contours[0][:, 0]])  # 轮廓的最大值
    top = min([i[1] for i in contours[0][:, 0]])  # 轮廓的最小值
    split_small_img = binary[top:bottom, 0:47]  # 图片切割， 顺序为[y0:y1, x0:x1]  # 将小图的方框切割出来
    template_rgb = big_img[top - 3:bottom + 3, 0:310]  # 图片切割， 顺序为[y0:y1, x0:x1]   # 根据小图y轴位置，去切割大图
    gray = cv2.cvtColor(template_rgb, cv2.COLOR_BGR2GRAY)
    ret, big_threshold = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)  #灰度
    res = cv2.matchTemplate(big_threshold, split_small_img, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # https://blog.csdn.net/firemicrocosm/article/details/48374979
    # 参考  # cv2.TM_CCOEFF 匹配 max_loc
    # y, x = split_small_img.shape[::-1]  # 倒叙
    # template_rgb = cv2.rectangle(template_rgb, max_loc, (max_loc[0]+x, max_loc[1]+y), (0,0,255), 1) # 画方框，必须画到原图
    # cv2.imshow("template_rgb", template_rgb)
    # cv2.imshow("big_img", big_img)
    # cv2.imshow("small_img", small_img)
    # cv2.waitKey(0)
    return max_loc[0]
