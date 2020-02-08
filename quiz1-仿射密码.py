#!/usr/bin/env python
# -*- coding: utf-8 -*
# @Author  :   Zyue
# @Time    :  2020/2/7 23:26
"""
仿射密码

参数选取：
    模数n=26+10=36 (26个字母+10个数字)，
    k2 = 学号后3位 mod n；k1 = 学号后4位 mod n,
    若k1与n不互素，则更新k1 <- k1+7 或 k1 -> k1-7。
加解密：
    加密自己名字的全拼和学号，再解密。
"""

ID = '03173666'
N = 36
INFO = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def gcd(a, b):
    """辗转相除法求最大公约数"""
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_reverse(a, m):
    """扩展欧几里得算法求模逆"""
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def true_k_prime(k):
    """保证k和N互素"""
    if gcd(N, k) != 1:
        k = (k - 7) % N
        return true_k_prime(k)
    else:
        return k


def confirm_params(ID):
    """确认k1,k2是否合法"""
    k1 = int(ID[-3:]) % N
    k2 = int(ID[-4:]) % N

    k1 = true_k_prime(k1)
    k2 = true_k_prime(k2)
    return k1, k2


def encrypt(data):
    """加密数据"""
    # 存放加密数据的序列
    data_sequence = []

    # 存放密文
    cipher = []

    # 将字母数字转化为整数序列
    for d in data:
        if d > '9':
            data_sequence.append(ord(d) - ord('a'))
        else:
            data_sequence.append(ord(d) - ord('0') + 26)

    # 加密
    for m in data_sequence:
        m = (m * k1 + k2) % N
        cipher.append(INFO[m])

    # print(data_sequence)
    # print(cipher)
    return ''.join(cipher)


def decode(data):
    """
    解密密文
    """
    # 存放解密数据的序列
    data_sequence = []

    # 存放明文
    message = []

    # 将字母数字转化为整数序列
    for d in data:
        if d > '9':
            data_sequence.append(ord(d) - ord('a'))
        else:
            data_sequence.append(ord(d) - ord('0') + 26)

    # 解密
    for m in data_sequence:
        m = find_mod_reverse(k1, N) * (m - k2) % N
        message.append(INFO[m])

    return ''.join(message)


if __name__ == "__main__":
    k1, k2 = confirm_params(ID)
    print('仿射密码的参数k1, k2为 %s, %s.' % (k1, k2))

    data = input("Input the data you want to encrypt : ").lower()
    print(encrypt(data))

    data = input("Input the data you want to decode : ").lower()
    print(decode(data))
