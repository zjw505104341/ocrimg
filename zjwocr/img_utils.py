# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/3 15:38

import cv2, numpy

def to_rgb(im):
    """
    图片转 RGB
    :param im: 图片 np.array
    :return: 图片 np.array
    """
    if len(im.shape) == 2:  # 灰度
        return cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    elif im.shape[2] == 4:  # PNG (RGBA)
        return cv2.cvtColor(im, cv2.COLOR_RGBA2RGB)
    assert len(im.shape) == 3 and im.shape[2] == 3  # 如果 Channel 不为3, 肯定出问题了
    return im


def loadimg(path_or_bytes, size=None):
    """
    加载图片
    :param path_or_bytes: 图片目录 / 字节
    :param size: 缩放图片 (width, height)
    :return: 图片 numpy.array (height, width, dim)
    """
    if isinstance(path_or_bytes, str):
        im = numpy.fromfile(path_or_bytes, dtype=numpy.uint8)
    elif isinstance(path_or_bytes, bytes):
        im = numpy.frombuffer(path_or_bytes, dtype=numpy.uint8)
    else:
        raise TypeError("图必须是路径或字节")

    im = cv2.imdecode(im, -1)
    if size is not None:
        im = cv2.resize(im, size, interpolation=cv2.INTER_AREA)
    return im