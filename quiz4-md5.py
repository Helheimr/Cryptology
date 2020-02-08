#!/usr/bin/env python
# -*- coding: utf-8 -*
# @Author  :   Zyue
# @Time    :  2020/2/8 20:23
"""
理解MD5、SHA-1算法的实现原理，通过采用现成的软件，
对实际数据进行Hash运算并验证，加深对MD5、SHA-1算法原理的认识与理解。
"""
from Cryptodome.Hash import MD5

message = b'xupt03176666zyue'

hash = MD5.new(message)
digest = hash.hexdigest()
print(digest)
