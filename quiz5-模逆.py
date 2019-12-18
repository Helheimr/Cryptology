# 编程实现快速模幂运算
# 编程实现求逆运算


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


def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e & 1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result


if __name__ == "__main__":
    # a = fastExpMod(5, 1003, 12)
    # print(a)
    print(findModReverse(5,12))
