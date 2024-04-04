'''
SỬ DỤNG ĐỊNH LÝ EULER ĐỂ TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏
Input: a = 34; m = 2249; n = 374
Tìm Output: b =
'''
import math

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

def tinhLuyThuaModulo(a, m, n):
    res = 1 # Khởi tạo kết quả
    a = a % n # Chuyển a thành a mod n
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n  # Nếu m là số lẻ, nhân b với a
        m = m // 2 # Hạ bậc lũy thừa m
        a = (a * a) % n  # Cập nhật a
    return res

def dinhLyEuler(a, m, n):
    if math.gcd(a, n) == 1:
        phi_n = phiEuler(n)
        m = m % phi_n
        return tinhLuyThuaModulo(a, m, n)
    else:
        return tinhLuyThuaModulo(a, m, n)

if __name__ == "__main__":
    a = int(input("Nhập a = "))
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    b = dinhLyEuler(a, m, n) # b = a^m mod n sử dụng Định lý Euler
    print("=> Output b = {}".format(b))
