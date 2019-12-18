import numpy as np
from operator import mod

# 加密密钥矩阵
K_LIST = [[8, 6, 9, 5],
          [6, 9, 5, 10],
          [5, 8, 4, 9],
          [10, 6, 11, 4]]


def deal_num(list_index, K_LIST):
    """E
    加密处理C＝KP
    """
    deal_list = [0, 0, 0, 0]
    for i in range(len(K_LIST)):
        for j in range(len(K_LIST[i])):
            deal_list[i] += list_index[j] * K_LIST[i][j]
        deal_list[i] = (deal_list[i] % 26)
    return deal_list


def encryption(clear_text):
    """
    加密时调用的函数
    :param clear_text:输入的明文
    :return: 加密后的密文
    """
    list_clear_text = list(clear_text.split(" "))
    cipher_list = []  # 用来存入密文
    # 明文每3个为一组，找出每组在字母表中的位置(用一个列表来保存)
    for i in range(len(list_clear_text)):
        if i % 3 == 0 and i+2 <= len(list_clear_text)-1:
            w = int(list_clear_text[i])
            x = int(list_clear_text[i+1])
            y = int(list_clear_text[i+2])
            z = int(list_clear_text[i+3])
            list_index = [w, x, y, z]
            # 调用deal_num函数进行加密 矩阵K与明文P运算得到密文C，即C＝KP
            deal_list = deal_num(list_index, K_LIST)
            cipher_list.extend(deal_list)

    return cipher_list


def decryption(cipher_text, K_OB):
    """
    加密时调用的函数
    :param cipher_text:输入的密文
    :return: 解密后的明文
    """
    list_cipher_text = list(cipher_text.split(" "))
    clear_list = []  # 用来存入明文
    # 明文每3个为一组，找出每组在字母表中的位置(用一个列表来保存)
    for i in range(len(list_cipher_text)):
        if i % 3 == 0 and i+2 <= len(list_cipher_text)-1:
            w = int(list_cipher_text[i])
            x = int(list_cipher_text[i+1])
            y = int(list_cipher_text[i+2])
            z = int(list_cipher_text[i+3])
            list_index = [w, x, y, z]
            # 调用deal_num函数进行加密 矩阵K与明文P运算得到密文C，即C＝KP
            deal_list = deal_num(list_index, K_OB)
            clear_list.extend(deal_list)

    return clear_list


if __name__ == "__main__":
    while True:
        choice = input("Please input E for encryption or D for decryption:")
        if choice == "E":
            clear_text = input("请输入明文(通过空格分割):")
            print("加密成功！密文:", encryption(clear_text))
        if choice == "D":
            # 计算逆矩阵
            K_OB = np.zeros(shape=(4, 4))
            K_NEW = np.linalg.inv(K_LIST)
            for i in range(len(K_NEW)):
                for j in range(len(K_NEW[i])):
                    K_OB[i][j] = int(mod(round(K_NEW[i][j]), 26))
            # print(K_OB)
            cipher_text = input("请输入密文(通过空格分割):")
            print("解密成功！明文:", decryption(cipher_text, K_OB))
