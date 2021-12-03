# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/3 13:14

# from setup import author, version
# print('name: {}, version {}'.format("zjw", "0.0.1"))

from zjwocr.ocr import ocr_api
import requests, time

url = 'http://credit.customs.gov.cn/ccppserver/verifyCode/creator?{}'.format(int(time.time() * 1000))
resp = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
},  verify=False, timeout=10)
checkCode = ocr_api({'图片': resp.content,'网站': '中国海关企业进出口信用信息公示平台'})
print(checkCode)