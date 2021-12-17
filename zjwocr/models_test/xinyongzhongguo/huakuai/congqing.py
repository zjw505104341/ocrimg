# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/17 9:13

import requests, time, base64, execjs, random
import cv2, numpy, re
from utils.Proxy import get_ip
from Crypto.Cipher import AES

proxies = get_ip()
headers = {
    'Host': 'www.xycq.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '65',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'Accept': '*/*',
    'Content-Type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://www.xycq.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.xycq.gov.cn/html/query/agree/list.html?navPage=1&isPage=true',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}


class Hua_kuai():
    
    def pkcs7padding(self, text):
        """
        明文使用PKCS7填充
        """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        # coding = chr(padding)
        return text + padding_text
    
    def get_encrypt(self, x_y_str, secretKey):
        """
        :param x_y_str:
        :param secretKey:
        :return: 获取aes密文值
        """
        cipher = AES.new(key=secretKey.encode('utf-8'), mode=AES.MODE_ECB)
        content_padding = self.pkcs7padding(x_y_str)
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result
    
    def requests_1(self):
        post_url_1 = 'https://www.xycq.gov.cn/captcha/captcha/get'
        post_json = {
            "captchaType": "blockPuzzle",
            "clientUid": None,
            "ts": int(time.time() * 1000)
        }
        rep_1 = requests.post(
            url=post_url_1,
            json=post_json,
            headers=headers,
            proxies=proxies,
            timeout=10
        )
        jigsawImageBase64 = rep_1.json()['repData']['jigsawImageBase64']
        originalImageBase64 = rep_1.json()['repData']['originalImageBase64']
        secretKey = rep_1.json()['repData']['secretKey']
        token = rep_1.json()['repData']['token']
        jigsawImage = base64.b64decode(jigsawImageBase64)
        originalImage = base64.b64decode(originalImageBase64)
        secretKey = secretKey
        token = token
        return jigsawImage, originalImage, secretKey, token
    
    def get_x_y(self, small_img, big_img):
        small_img = numpy.frombuffer(small_img, dtype=numpy.uint8)
        big_img = numpy.frombuffer(big_img, dtype=numpy.uint8)
        small_img = cv2.imdecode(small_img, cv2.IMREAD_COLOR)
        big_img = cv2.imdecode(big_img, cv2.IMREAD_COLOR)
        # small_img = cv2.imread(small_img) # 小图
        # big_img = cv2.imread(big_img)  #　 大图
        
        gray = cv2.cvtColor(small_img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)  # 灰度
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测
        bottom = max([i[1] for i in contours[0][:, 0]])  # 轮廓的最大值
        top = min([i[1] for i in contours[0][:, 0]])  # 轮廓的最小值
        split_small_img = binary[top:bottom, 0:47]  # 图片切割， 顺序为[y0:y1, x0:x1]  # 将小图的方框切割出来
        template_rgb = big_img[top - 3:bottom + 3, 0:310]  # 图片切割， 顺序为[y0:y1, x0:x1]   # 根据小图y轴位置，去切割大图
        gray = cv2.cvtColor(template_rgb, cv2.COLOR_BGR2GRAY)
        ret, big_threshold = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)  # 灰度
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
        return max_loc
    
    def requests_2(self, pointJson, token):
        post_url_2 = 'https://www.xycq.gov.cn/captcha/captcha/check'
        post_json_2 = {
            "captchaType": "blockPuzzle",
            "pointJson": pointJson,
            "token": token,
            "clientUid": None,
            "ts": int(time.time() * 1000)
        }
        rep_2 = requests.post(url=post_url_2, json=post_json_2, headers=headers, proxies=proxies, timeout=10)
        return rep_2.json()
    
    def requests_3(self, name):
        post_url_3 = 'https://www.xycq.gov.cn/html/query/querySensitive.html'
        post_json_3 = {'keywords': name}
        rep_3 = requests.post(url=post_url_3, data=post_json_3, headers=headers, proxies=proxies, timeout=10)
        cookies = requests.utils.dict_from_cookiejar(rep_3.cookies)
        return cookies
    
    def requests_4(self, captchaVerification, name, cookies):
        post_url_4 = 'https://www.xycq.gov.cn/html/query/agree/list.html?navPage=1&iframe=false'
        post_json_4 = {
            'pageNo': '',
            'captchaVerification': captchaVerification,
            'isPage': 'false',
            'contentType': '1',
            'contentValue': name,
        }
        
        rep_4 = requests.post(url=post_url_4, data=post_json_4, headers={
            'Host': 'www.xycq.gov.cn',
            'Connection': 'keep-alive',
            'Content-Length': '328',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://www.xycq.gov.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.xycq.gov.cn/html/query/agree/list.html?navPage=1&isPage=true',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            
        }, proxies=proxies, cookies=cookies, timeout=10)
        count_name =  rep_4.text.count('重庆市涪陵区鑫禄嘉酒店管理有限公司',0,-1)
        return count_name
    
    def img_save(self, jigsawImage, originalImage):
        with open(r'originalImage.png', 'wb') as wb:
            wb.write(originalImage)
        
        with open(r'jigsawImage.png', 'wb') as wb:
            wb.write(jigsawImage)
    
    def get_x_y_str(self, x):
        x = round(float(x) + random.random(), 2)
        x_y_str = '{"x":%s,"y":5}' % (x)
        return x_y_str
    
    def run(self):
        # name = "重庆华康物业管理有限公司"
        # name = "城口县兰熠建筑设备租赁有限公司"
        # # name = "重庆恒碧房地产开发有限公司"
        # # name = "重庆宽毅农业发展有限公司"
        
        name = "重庆市涪陵区鑫禄嘉酒店管理有限公司"
        jigsawImage, originalImage, secretKey, token = self.requests_1()  # 第一次请求
        print('获取 图片 secretKey token 成功: ', secretKey, token)
        self.img_save(jigsawImage, originalImage)  # 图片保存
        x, y = self.get_x_y(jigsawImage, originalImage)  # 获取图片的　ｘ，ｙ
        x_y_str = self.get_x_y_str(x)  # 获取x-y 的组合 str
        print('缺口距离计算成功：', x_y_str)
        pointJson_1 = self.get_encrypt(x_y_str, secretKey)  # 获取aes密文值,后期请求需要
        rep_2_data = self.requests_2(pointJson_1, token)
        if rep_2_data['success']:
            print('验证码通过:', rep_2_data)
            cookies = self.requests_3(name)
            print('cookie 获取成功:', cookies)
            captchaVerification = base64.b64encode(self.get_encrypt('%s---%s' % (token, x_y_str), secretKey).encode('utf-8'))  # 获取第二个加密对象,下毒 b64encode
            count_name = self.requests_4(captchaVerification, name, cookies)  # 获取搜索数据
            print('name 出现次数为：', count_name, )


if __name__ == '__main__':
    obj = Hua_kuai()
    obj.run()
