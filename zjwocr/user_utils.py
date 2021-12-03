# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/3 15:37
import io
from PIL import Image

def is_user_data_type(data):
    if isinstance(data, dict):
        if isinstance(data["图片"], str):
            if "<"  in data.get('图片') or '>' in data.get("图片"):
                raise TypeError('传入的路径不可以携带<,> or 传入图片,不是html')
        if data.get("网站") and data.get("图片"):
            return data
        else:
            raise TypeError('兄弟,你皮呐？ 在皮揍你，给我传空值？')
    else:
        raise TypeError('data 输入值必须是 dict (字典) ,请输入 {"img":"","domain",""}')



def credit_img_util(data):
    im = Image.open(io.BytesIO(data["图片"]))
    im.seek(8)
    img_byte = io.BytesIO()
    im.save(img_byte, format='PNG')
    binary_content = img_byte.getvalue()
    return {"网站": data['网站'], "图片": binary_content}

def is_user_model(data):
    if data["网站"] == "中国海关企业进出口信用信息公示平台":   # http://credit.customs.gov.cn/
        if isinstance(data["图片"], str):
            data = credit_img_util(data)
        elif isinstance(data["图片"], bytes):
            data = credit_img_util(data)
        else:
            raise TypeError('图必须是路径或字节')
        return data
    else:
        raise TypeError('现在只有 中国海关企业进出口信用信息公示平台 的验证码，静待作者后续版本升级')
