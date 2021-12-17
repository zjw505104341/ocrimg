# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/17 19:35


import base64, execjs
from Crypto.Cipher import AES

def pkcs7padding(text):
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


def get_encrypt(data, secretKey):
    data = str(data)
    cipher = AES.new(key=secretKey.encode('utf-8'), mode=AES.MODE_ECB)
    content_padding = pkcs7padding(data)
    encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


js_all = r"""
let CryptoJS = require("crypto-js");
function aesEncrypt(word,keyWord){
  // var keyWord = keyWord || "XwKsGlMcdPMEhR1B"
  var key = CryptoJS.enc.Utf8.parse(keyWord);
  var srcs = CryptoJS.enc.Utf8.parse(word);
  var encrypted = CryptoJS.AES.encrypt(srcs, key, {mode:CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7});
  return encrypted.toString();
}
"""
# pointJson_1 = execjs.compile(js_all).call("aesEncrypt", '{"x":12.5,"y":5}', 'zu72OIbf9AS2qthA')
# pointJson_2 = get_encrypt('{"x":12.5,"y":5}', 'zu72OIbf9AS2qthA')
# print(pointJson_1)
# print(pointJson_2)



