# 注释头文件
# 分别对自己的学号，姓名全拼进行加解密(分别在五种不同工作模式下)

from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from binascii import b2a_base64, a2b_base64

MODE = ['MODE_ECB', 'MODE_CBC', 'MODE_CFB', 'MODE_OFB', 'MODE_CTR',
        'MODE_OPENPGP', 'MODE_CCM', 'MODE_EAX', 'MODE_SIV0', 'MODE_GCM1', 'MODE_OCB2']
message = b'xiyou03173xxxlyuan'


class DES_Encrypt(object):
    def __init__(self, key, mode):
        self.mode = DES.MODE_CBC
        # key没有填充，必须传入16字节
        self.key = key

    def encrypt(self, text):
        texts = pad(text, DES.block_size)
        aes = DES.new(self.key, self.mode, self.key)
        cipher = aes.encrypt(texts)
        # 这里会多返回一个换行符，也不知道咋改，将就用[:-1]
        return str(b2a_base64(cipher), encoding="utf-8")[:-1]

    def decrypt(self, text):
        texts = a2b_base64(text)
        aes = DES.new(self.key, self.mode, self.key)
        cipher = aes.decrypt(texts)
        return str(unpad(cipher, DES.block_size), encoding='utf-8')


if __name__ == "__main__":

    # key = b'\xf4QJ\xefJ\x10a \x85\xe7"F\xbfZ|\xde'
    for mode in MODE:
        key = get_random_bytes(8)
        print('DES Mode: ' + str(mode))
        a = DES_Encrypt(key, mode).encrypt(message)
        print('Encrypted Data: ' + a)
        b = DES_Encrypt(key, mode).decrypt(a)
        print('Decrypted Data: ' + b + '\n')
