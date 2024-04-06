'''
Thuật toán RSA - Bài toán 2:
Input: p, q, e
Output:
a) PU = {e, n} =
b) PR = {d, n} =
c) Ba mã: C =
d) An giải mã C: M’ =
'''

import math

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

def phiEuler(n):
    res = n #Khởi tạo phi(n) = n
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            res = res * (1 - 1.0/i) # Giảm phi (n)
            while n%i == 0:
                n //= i # ta loại bỏ tất cả thừa số i khỏi n
    if n > 1:
        res -= res/n
    return int(res)

if __name__ == "__main__":
    p = int(input("Nhập p = "))
    q = int(input("Nhập q = "))
    e = int(input("Nhập e = "))
    print("=" * 20)
    n = p * q
    phi_n = phiEuler(n)
    d = euclidMoRong(e, phi_n)

    # a) Khóa công khai PU = {e, n}
    print(f"a) Khóa công khai PU = ({e},{n})")
    # b) Khóa riêng PR = {d, n}
    print(f"b) Khóa bí mật PR = ({d}, {n})")
    print("=" * 20)

    # c) Ba Mã hóa gửi cho An
    M = int(input("Nhập thông điệp M = "))
    C = tinhMod(M,e,n)
    print(f"c) Ba mã hóa thông điệp M = {M} với C = M^e mod n = {C}")

    # d) An giải mã
    M_giai = tinhMod(C, d, n)
    print(f"d) An giải mã C: M' = {M_giai}")

