#!/usr/bin/env python
# -*- coding: utf-8 -*
# @Author  :   Zyue
# @Time    :  2020/2/8 20:23
"""
分别对自己的学号，姓名全拼做加解密
"""
import base64

from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Cryptodome.PublicKey import RSA

# 数据加密
message = b'xupt03176666zyue'
with open('rsa.pub', 'rb') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    cipher_text = base64.b64encode(cipher_obj.encrypt(message))
    print('cipher test: ', cipher_text)

print()
# 数据解密
with open('rsa.key', 'rb') as f:
    private_key = f.read()
    rsa_key_obj = RSA.importKey(private_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    random_generator = Random.new().read
    plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator)
    print('plain text: ', plain_text)
