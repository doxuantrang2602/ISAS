'''
TÍNH CÁC BIỂU THỨC MODULO CƠ BẢN
        𝑨𝟏 = (a^x + b^y) 𝒎𝒐𝒅 n
        𝑨2 = (a^x - b^y) 𝒎𝒐𝒅 n
        𝑨3 = (a^x * b^y) 𝒎𝒐𝒅 n
        𝑨4 = (b^y)^-1 𝒎𝒐𝒅 n
        𝑨5 = (a^x / b^y) 𝒎𝒐𝒅 n
Input: a = 43; b = 53; x = 308; y = 455; n = 179
Tìm Output: A1 = ; A2 = ; A3 = ; A4 = ; A5 = ?
'''

def tinhLuyThuaModulo(a, m, n):
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
    res = 0
    if r1 == 1:
        res = y1
    else: res = None
    # Nếu res là số âm
    if res is not None and res < 0:
        res += n
    return res

if __name__ == "__main__":
    a, b, x, y, n = 43, 53, 308, 455, 179

    # Tính các biểu thức modulo
    A1 = (tinhLuyThuaModulo(a, x, n) + tinhLuyThuaModulo(b, y, n)) % n
    A2 = (tinhLuyThuaModulo(a, x, n) - tinhLuyThuaModulo(b, y, n)) % n
    A3 = (tinhLuyThuaModulo(a, x, n) * tinhLuyThuaModulo(b, y, n)) % n
    A4 = euclidMoRong(tinhLuyThuaModulo(b, y, n), n)
    A5 = (tinhLuyThuaModulo(a, x, n) * euclidMoRong(tinhLuyThuaModulo(b, y, n), n)) % n

    print("=> A1 =", A1)
    print("=> A2 =", A2)
    print("=> A3 =", A3)
    print("=> A4 =", A4)
    print("=> A5 =", A5)
