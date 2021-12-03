# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/3 11:38

from setuptools import find_packages, setup
# version = '0.0.1'
# author = 'zhoujunwei'
setup(
    name='zjwocr',  #　包的名字
    version='0.0.3',
    description='test',
    author='zhoujunwei',
    author_email='505104341@qq.com',
    url='https://github.com/zjw505104341/ocrimg',
    #packages=find_packages(),
    packages=['zjwocr'], # 包的目录
    #install_requires=['requests'],
)
