# # coding = utf-8
# from Crypto.Cipher import AES
# import base64
# import requests
# import json


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
import base64
from Crypto.Cipher import AES
from pprint import pprint


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return str(ciphertext)


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16)**int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(chr(xx)))[2:]), os.urandom(size))))[0:16]


url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token='
headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/'
}
text = {
    'username': '邮箱',
    'password': '密码',
    'rememberLogin': 'true'
}
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'
text = json.dumps(text)
secKey = createSecretKey(16)
encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
encSecKey = rsaEncrypt(secKey, pubKey, modulus)
data = {
    'params': encText,
    'encSecKey': encSecKey
}

req = requests.post(url, headers=headers, data=data)
pprint(req.json())
for content in req.json()['comments']:
    print (content['content'].encode('utf-8'))
print (req.json()['total'])
# # second_param = "010001"
# # third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5f" \
# #               "f68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629" \
# #               "ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7" \
# #               "f0c3685b7a46bee255932575cce10b424d813cfe487" \
# #               "5d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# # forth_param = "0CoJUm6Qyw8W8jud"
# #
# #
# # def get_params(offset,limit):
# #     iv = "0102030405060708"
# #     first_key = forth_param
# #     second_key = 16 * 'F'
# #     first_param='{rid:"", offset:"%s", total:"%s", limit:"%s", csrf_token:""}' %(20,'false',20)
# #     h_encText = AES_encrypt(first_param, first_key, iv)
# #     h_encText = AES_encrypt(h_encText, second_key, iv)
# #     return h_encText
# #
# #
# # def AES_encrypt(text, key, iv):
# #     pad = 16 - len(text) % 16
# #     # print(isinstance(text,str))
# #     # print("======")
# #     # print(isinstance(pad * chr(pad),str))
# #     text =  pad * chr(pad)+text
# #     encryptor = AES.new(key, AES.MODE_CBC, iv)
# #     encrypt_text = encryptor.encrypt(text)
# #     encrypt_text = base64.b64encode(encrypt_text)
# #     return encrypt_text.decode()
# #
# # def get_encSecKey():
# #     encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4" \
# #                 "c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5" \
# #                 "f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3" \
# #                 "f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
# #     return encSecKey
# #
# # def get_json(url, params, encSecKey):
# #     data = {
# #          "params": params,
# #          "encSecKey": encSecKey
# #     }
# #     print(data)
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
# #         'Content-Type': 'application/x-www-form-urlencoded',
# #         'Host': 'music.163.com',
# #         'Referer':'https://music.163.com/video?id=3E93122371078D86ACA39C9620C3882B'
# #     }
# #
# #     response = requests.post(url, headers=headers, data=data)
# #     return response.content
# #
# #
# # if __name__ == '__main__':
# #     type='R_VI_62_'  # video is R_VI_62_ song is R_SO_4_
# #     id='3E93122371078D86ACA39C9620C3882B'
# #     url='https://music.163.com/weapi/v1/resource/comments/{type}{id}?csrf_token='
# #     for page in range(0,1):
# #         params=get_params(10,10)
# #         encSecKey=get_encSecKey()
# #         url=url.format(type=type,id=id)
# #         print(url)
# #         json_text=get_json(url,params,encSecKey)
# #         print(json_text)
# #         json_dict=json.loads(json_text)
# #         # print(json_dict)
# #
# #
# #
# #
