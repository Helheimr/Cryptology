# Hill密码
# 参数选取：密钥矩阵和明文/密文的元素均取自Z 26
# 密钥矩阵为:    [8, 6, 9, 5]
#               [6, 9, 5, 10]
#               [5, 8, 4, 9]
#               [10, 6, 11, 4]
# 加解密：若明文为7,8,11,11, 计算密文；若密文为9,8,8,24，计算明文。

from numpy import *
import numpy as np

key = [[8, 6, 9, 5],
       [6, 9, 5, 10],
       [5, 8, 4, 9],
       [10, 6, 11, 4]]
message = [7, 8, 11, 11]
N = 26


def gcd(a, b):
    # 辗转相除法求最大公约数
    while a != 0:
        a, b = b % a, a
    return b


def findModReverse(a, m):
    # 这个扩展欧几里得算法求模逆
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3//v3
        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
    return u1 % m


def get_cipher_text(message):
    cipher_text = mat(message) * mat(key)
    cipher_text = array(cipher_text)
    for i in range(len(cipher_text)):
        cipher_text[i] = cipher_text[i] % 26
    print(cipher_text)
    return cipher_text


def get_message():
    key22 = mat(key)
    # print(key22)
    key0 = key22.I
    # print(key0)
    cipher = get_cipher_text(message)
    mess0 = mat(cipher) * key0
    mess0 = array(mess0)
    for i in range(len(mess0)):
        mess0[i] = mess0[i] % N
    print(mess0)


if __name__ == "__main__":
    # get_cipher_text(message)
    get_message()
    