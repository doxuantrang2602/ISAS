import math

def tinhMod(a, xA, q):
    return pow(a, xA, q) # a^xA mod q

def tinhLuyThuaModulo(a,m,n):
    D = {}
    i = 1
    while i <= m:
        D[i] = pow(a, i, n)
        i *= 2
    res = 1
    for p in sorted(D.keys(), reverse=True):
        if m >= p:
            res = (res * D[p]) % n
            m -= p
    return res

def tinhLuyThuaModulo2(a, m, n):
    res = 1 # Khởi tạo kết quả
    a = a % n # Chuyển a thành a mod n
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n  # Nếu m là số lẻ, nhân b với a
        m = m // 2 # Hạ bậc lũy thừa m
        a = (a * a) % n  # Cập nhật a
    return res

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

def ptThuaSoNguyenTo(n):
    lst = []
    p = 2
    while n > 1:
        while n % p == 0:
            lst.append(p)
            n //= p
        p += 1
    return lst

def phiEuler(n):
    factors = ptThuaSoNguyenTo(n)
    res = n
    for p in factors:
        res *= (1 - 1.0/p)
    return int(res)

def phi(n):
    res = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            res += 1
    return res

def modNghichDao(a, q):
    for i in range(1, q):
        if (a * i) % q == 1:
            return i
    return None
