'''
Mật mã ElGamal
Input: q là một số nguyên tố, a là căn nguyên thủy của q, xA, k, M
Output:
a) PU = {q, a, YA}
a) Ba mã hóa M, bản mã là (C1, C2)
b) An giải bản mã (C1, C2)?

Giả sử An và Ba trao đổi bằng hệ mật mã ElGamal, có các giá trị chung là
q = 7001 là một số nguyên tố, a = 6 là căn nguyên thủy của q.
An chọn khóa riêng là xA = 382
Hãy cho biết
a) Khóa công khai của An: PU = {q, a, YA} với yA =
b) Ba chọn số k = 589 để mã hóa bản tin M = 442 gửi cho An. Bản mã là (C1, C2) =
c) Cách An giải bản mã (C1, C2)?
'''
import math
from builtins import input

def tinhMod(a, xA, q):
    return pow(a, xA, q) # a^xA mod q

def tinhModNghichDao(a, q):
    for i in range(1, q):
        if (a*i) % q == 1:
            return i
    return None

if __name__ == "__main__":
    q = int(input("Nhập q = "))
    a = int(input("Nhập a = "))
    xA = int(input("Nhập xA = "))
    # a) Khóa công khai của An: PU = {q, a, YA} với yA = a^xA mod q
    yA = tinhMod(a,xA, q)
    print("Khóa công khai PU = {{q, a, yA}} = {{ {}, {}, {} }}".format(q, a, yA))
    print("="*50)

    # b) Ba chọn số k để mã hóa bản tin M gửi cho An. Bản mã là (C1, C2) =
    # C1 = a^k mod q, C2 = KM mod q với K = yA^k mod q
    k = int(input("Nhập k = "))
    M = int(input("Nhập M = "))
    K = tinhMod(yA, k, q)
    C1 = tinhMod(a, k, q)
    C2 = tinhMod(K*M, 1, q)
    print("Bản mã (C1, C2) là: ({}, {})".format(C1, C2))
    print("=" * 50)

    #c) Cách An giải bản mã (C1, C2)?
    # K = C1^xA mod q
    # M = (C2*K^-1) mod q = (C2 mod q * K^-1 mod q) mod q
    K_giaiMa = tinhMod(C1, xA, q)
    #M_giai = ((C2 % q) * tinhModNghichDao(K_giaiMa, q)) % q
    M_giaiMa = tinhMod(tinhMod(C2,1,q) * tinhModNghichDao(K_giaiMa,q), 1, q)
    print("An giải bản mã (C1, C2) được K = {}, M = {}".format(K_giaiMa, M_giaiMa))



