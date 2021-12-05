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
    author='周军威',
    author_email='505104341@qq.com',
    url='https://github.com/zjw505104341/ocrimg',
    packages=find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'torch',
        'torchaudio',
        'torchvision'
        'numpy'
        'opencv-python'
        'Pillow'
        'requests'
    ], # 依赖包
    python_requires='>=3.7',# python 的版本
    include_package_data=True, #
    install_package_data=True,
)
