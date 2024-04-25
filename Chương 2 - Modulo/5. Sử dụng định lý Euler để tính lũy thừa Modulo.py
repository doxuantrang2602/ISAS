'''
SỬ DỤNG ĐỊNH LÝ EULER ĐỂ TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏
Input: a = 34; m = 2249; n = 374
Tìm Output: b = 34
'''
from CacHamBoTro import phiEuler, tinhLuyThuaModulo
import math

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
    b = dinhLyEuler(a, m, n)
    print("=> Output b = {}".format(b))
