def tinhLuyThuaModulo(a, m, n):
    res = 1 # Khởi tạo kết quả
    a = a % n # Chuyển a thành a mod n
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n  # Nếu m là số lẻ, nhân b với a
        m = m // 2 # Hạ bậc lũy thừa m
        a = (a * a) % n  # Cập nhật a
    return res

def euclidMoRong(n, a):
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    if r1 == 1:
        return y1 if y1 > 0 else y1 + n
    else:
        return None

def ptThuaSoNguyenTo(n):
    s = set()
    p = 2
    while n > 1:
        while n % p == 0:
            s.add(p)
            n //= p
        p += 1
    return s
