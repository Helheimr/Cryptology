# 被生成元计算搞崩了，计算量太大，萌生此代码
import math
import itertools

def findModReverse(a, m):
    for b in itertools.count(1):
        if (a*b) % m == 1:
            return b


def main(dot1, dot2):
    global i
    if i <= 13:
        a = 13
        p = 23
        if dot2 == dot1:
            nmd = ((dot1[0]*dot1[0]*3+a)*findModReverse(2*dot1[1], p)) % p
        else:
            nmd = ((dot2[1]-dot1[1])*findModReverse(dot2[0]-dot1[0], p)) % p
        # print(nmd)
        x3 = (nmd*nmd - dot1[0] - dot2[0]) % p
        y3 = (nmd*(dot1[0] - x3) - dot1[1]) % p

        print("{}g = ({},{})".format(i, x3, y3))
        i = i + 1
        main(dot1, [x3, y3])

def two(dot1,dot2):
    a = 13
    p = 23
    if dot2 == dot1:
        nmd = ((dot1[0]*dot1[0]*3+a)*findModReverse(2*dot1[1], p)) % p
    else:
        nmd = ((dot2[1]-dot1[1])*findModReverse(dot2[0]-dot1[0], p)) % p
    # print(nmd)
    x3 = (nmd*nmd - dot1[0] - dot2[0]) % p
    y3 = (nmd*(dot1[0] - x3) - dot1[1]) % p
    print("({},{})".format(x3, y3))


if __name__ == "__main__":
    i = 2
    dotg = [10, 5] 
    # main(dotg, dotg)
    # two([20,5] ,[18,19])
    # t= findModReverse(11,101)
    t = (1776)%101
    print(t)
    
