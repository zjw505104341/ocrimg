# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/17 20:51
import os, sys, datetime, platform, traceback, time, uuid, hashlib, math, re

if platform.system().lower() == 'linux':
    sys.path.append("/home/zhoujunwei/spider")
get_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(get_path)))
import requests
from lxml import etree
from utils.log import send_log_ali
from utils.send_requests import get_response