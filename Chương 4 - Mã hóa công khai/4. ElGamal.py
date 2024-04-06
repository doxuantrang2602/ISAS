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

from builtins import input

def tinhMod(a, xA, q):
    return pow(a, xA, q) # a^xA mod q

def euclidMoRong(a, n):
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while r2 != 0:
        q = r1 // r2  # Tính thương
        r1, r2 = r2, r1 - q * r2  # Cập nhật r
        x1, x2 = x2, x1 - q * x2  # Cập nhật x
        y1, y2 = y2, y1 - q * y2  # Cập nhật y
    if r1 == 1:
        res = y1
    else: res = None
    # Nếu res là số âm
    if res is not None and res < 0:
        res += n
    return res

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
    M_giaiMa = (C2%q * euclidMoRong(K_giaiMa,q)) % q
    print("An giải bản mã (C1, C2) được K = {}, M = {}".format(K_giaiMa, M_giaiMa))

