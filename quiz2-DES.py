#!/usr/bin/env python
# -*- coding: utf-8 -*
# @Author  :   GaoAnQi
# @Desc    :  分别对自己的学号，姓名全拼进行DES加解密(分别在五种不同工作模式下)

from Cryptodome.Cipher import DES
from Cryptodome.Util import Counter
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes


def ECB():
    message = input('请输入明文（你的学号或姓名全拼）：')
    message = message.encode('gbk')
    
    # 随机生成8字节（即128位）的加密密钥
    key = get_random_bytes(8)
    # print(key)
    
    # 实例化加密套件，使用ECB模式
    cipher = DES.new(key, DES.MODE_ECB)
    
    # 对内容进行加密，pad函数用于分组和填充
    encryption = cipher.encrypt(pad(message, DES.block_size))
    print("加密密文为:", encryption)
    
    # 解密
    decryption = unpad(cipher.decrypt(encryption), DES.block_size)
    print("解密明文为:", decryption.decode('utf-8'))


def CBC():
    message = input('请输入明文（你的学号或姓名全拼）：')
    message = message.encode('gbk')
    
    # 随机生成8字节（即128位）的加密密钥
    key = get_random_bytes(8)
    # print(key)
    
    # 实例化加密套件，使用CBC模式
    cipher = DES.new(key, DES.MODE_CBC)
    # print(cipher.iv)
    
    # 对内容进行加密，pad函数用于分组和填充
    encryption = cipher.encrypt(pad(message, DES.block_size))
    print("加密密文为:", encryption)
    
    # 解密
    iv = cipher.iv
    
    # 实例化加密套件
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decryption = unpad(cipher.decrypt(encryption), DES.block_size)
    print("解密明文为:", decryption.decode('utf-8'))


def CTR():
    message = input('请输入明文（你的学号或姓名全拼）：')
    message = message.encode('gbk')
    
    # 随机生成8字节（即128位）的加密密钥
    key = get_random_bytes(8)
    # print(key)
    
    # 实例化加密套件，使用CTR模式
    cipher = DES.new(key, DES.MODE_CTR, counter=Counter.new(128, initial_value=0))
    
    # 对内容进行加密，pad函数用于分组和填充
    encryption = cipher.encrypt(message)
    print("加密密文为:", encryption)
    
    # 实例化加密套件
    cipher = DES.new(key, DES.MODE_CTR, counter=Counter.new(128, initial_value=0))
    
    # 解密
    decryption = cipher.decrypt(encryption)
    print("解密明文为:", decryption.decode('utf-8'))


def CFB():
    message = input('请输入明文（你的学号或姓名全拼）：')
    message = message.encode('gbk')
    
    # 随机生成8字节（即128位）的加密密钥
    key = get_random_bytes(8)
    # print(key)
    
    # 实例化加密套件，使用CFB模式
    cipher = DES.new(key, DES.MODE_CFB)
    # print(cipher.iv)
    
    # 对内容进行加密，pad函数用于分组和填充
    encryption = cipher.encrypt(pad(message, DES.block_size))
    print("加密密文为:", encryption)
    
    # 解密
    iv = cipher.iv
    
    # 实例化加密套件
    cipher = DES.new(key, DES.MODE_CFB, iv)
    decryption = unpad(cipher.decrypt(encryption), DES.block_size)
    print("解密明文为:", decryption.decode('utf-8'))


def OFB():
    message = input('请输入明文（你的学号或姓名全拼）：')
    message = message.encode('gbk')
    
    # 随机生成8字节（即128位）的加密密钥
    key = get_random_bytes(8)
    # print(key)
    
    # 实例化加密套件，使用OFB模式
    cipher = DES.new(key, DES.MODE_OFB)
    # print(cipher.iv)
    
    # 对内容进行加密，pad函数用于分组和填充
    encryption = cipher.encrypt(pad(message, DES.block_size))
    print("加密密文为:", encryption)
    
    # 解密
    iv = cipher.iv
    
    # 实例化加密套件
    cipher = DES.new(key, DES.MODE_OFB, iv)
    decryption = unpad(cipher.decrypt(encryption), DES.block_size)
    print("解密明文为:", decryption.decode('utf-8'))


while True:
    choice = int(input(" 1 for ECB\n 2 for CBC\n 3 for CTR\n 4 for CFB\n 5 for OFB\n Please choose:"))
    if choice == 1:
        ECB()
    if choice == 2:
        CBC()
    if choice == 3:
        CTR()
    if choice == 4:
        CFB()
    if choice == 5:
        OFB()
