# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   Zyue
# @Time    :  2020/2/8 13:54
"""LFSR
联结多项式1： p(x) = 1 + x + x7
联结多项式2： q(x) = 1+x2 + x4 + x7
1000001   0101001
（1）	分别画出上列两个联结多项式对应的LFSR结构图，
（2）	编程实现输出序列，并给出序列的周期，
（3）	将自己的姓名全拼和学号分别用上面两个输出序列进行加解密。
"""

LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']  # 把英文字母和十进制数字的对应关系存进一个数组中


class LFSR:
    def __init__(self, seq):
        """实现LFSR加密

        :param seq: 反馈系数
        :param data: 用于加密或者解密的数据
        """
        self.seq = list(seq)
        self.data = ''
        # 得到反馈所需要的索引
        self.feedback_indexs = [i for i in range(
            len(self.seq)) if self.seq[i] == '1']
        # 是否打印反馈序列
        self.true_print = False

    def encrypt_lfsr(self):
        """加密或解密数据"""
        # 把需要加密的数据换位成二进制
        b_data = ['{:06b}'.format(LIST.index(d)) for d in self.data]
        b_data = list("".join(b_data))  # 将列表[[],[]..] 化为 [..,..]
        # 计算长度，计算密钥
        data_length = len(b_data)
        # 处理初始值换位成二进制
        init = int(input("输入初始状态数字(十进制):"))
        init = list('{:07b}'.format(init))
        # 生成数据等长的密钥
        if input('是否打印反馈序列(1 or 0):') == '1':
            self.true_print = True
        key = []
        for i in range(data_length):
            init, out = self.cycle(init)
            key.append(out)
        print('密钥为：' + ''.join(key))

        # 计算二进制密文
        cipher_b_data = [str(int(key[i]) ^ int(b_data[i]))
                         for i in range(data_length)]
        # 将二进制分组
        cipher_b_data = ["".join(cipher_b_data[i:i + 6])
                         for i in range(0, data_length, 6)]
        # 换位为字符
        cipher_data = [LIST[int(cipher, 2)] for cipher in cipher_b_data]
        cipher_data = ''.join(cipher_data)
        print('密文为：' + cipher_data)
        print('-' * 50)

    def cycle(self, init_status):
        """根据初始态和反馈参数循环移位下一状态

        :param init_status: 初始态
        :return: 返回输出值和下一个状态
        """
        if self.true_print:
            # 打印每一状态，包括初始态
            print(''.join(init_status))

        # 得到反馈值即最高位
        feedback_value = int(init_status[self.feedback_indexs[0]])
        for i in range(len(self.feedback_indexs) - 1):
            feedback_value = feedback_value ^ int(
                init_status[self.feedback_indexs[i + 1]])
        # 输出值为最低位
        out = init_status[-1]
        # 倒序遍历
        for i in range(len(init_status))[::-1]:
            if i != 0:
                init_status[i] = init_status[i - 1]
            else:
                init_status[i] = str(feedback_value)

        return init_status, out


if __name__ == '__main__':
    seq = input('请输入反馈序列(例1001101)：')
    lfsr = LFSR(seq)
    while 1:
        choice = input("加密/解密输入e，退出输入q:")
        if choice == "e":
            lfsr.data = input("请输入数据:")
        if choice == 'q':
            break
        lfsr.encrypt_lfsr()
        # 初始化参数
        lfsr.true_print = False
