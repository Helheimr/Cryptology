# 置换密码
# 参数选取：分组长度为7；置换关系随机选取；
# 加解密：加密自己名字的全拼和学号（长度不足时后面全补填充长度），再解密。

import random
import re
N = 7


def substitution(data, encrypt_seq):
    '''
    置换data，采用encrypt_seq的顺序
    '''
    # 存放密文
    cipher = []

    # 加密数据
    data_split = [data[i:i+N] for i in range(0, len(data), N)]
    # 填充最后一个分组
    data_split[-1] = data_split[-1].ljust(N)

    # 遍历分组，置换每个分组
    print(data_split)
    for split in data_split:
        for seq in encrypt_seq:
            cipher.append(split[seq-1])

    cipher = ''.join(cipher)
    # 不能去除空格，这样会导致 t-n- 的顺序 识别为 tn--
    # 输出的时候可以去除填充，但处理数据的时候，绝对不行！ 
    # cipher = re.sub(r'\s+', '', cipher)
    return cipher


if __name__ == "__main__":
    data = 'zhouyang0317xxxx'
    data = re.sub(r'\s+', '', data)

    # 生成随机置换关系
    encrypt_seq = [i for i in range(1,8)]
    random.shuffle(encrypt_seq)
    # encrypt_seq = [4, 1, 3, 7, 2, 6, 5]
    print('Encrypt Sequence : ' + str(encrypt_seq))

    # 置换消息
    ciphertext = substitution(data, encrypt_seq)
    print('Ciphertext : ' + ciphertext)

    # 获取解密密钥
    decode_seq = [None]*N
    i = 1
    for seq in encrypt_seq:
        decode_seq[seq-1] = i
        i = i + 1
    print('------------------------------')
    print('Decode Sequence : ' + str(decode_seq))

    # 解密置换过的消息
    # seq = input('Input decode Sequence : ')
    print('Ciphertext : ' + substitution(ciphertext, decode_seq))
