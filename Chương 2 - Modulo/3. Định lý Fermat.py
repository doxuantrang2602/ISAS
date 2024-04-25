'''
SỬ DỤNG ĐỊNH LÝ FERMAT ĐỂ TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏
Input: a = 373; m = 851; n = 6211
Tìm Output: b =
'''

from CacHamBoTro import tinhLuyThuaModulo
import math

def checkPrime(p):
    if (p < 2):
        return True
    for i in range(2, int(math.sqrt(p)+1)):
        if p % i == 0:
            return False
    return True

def dinhLyFermat(a,m,n):
    if not checkPrime(n) or a % n == 0:
        print("Không thể áp dụng định lý Fermat")
    if a >= n:
        a = a % n
    m = m % (n - 1)
    res = tinhLuyThuaModulo(a, m, n)
    return res

if __name__ == "__main__":
    a = 373
    m = 851
    n = 6211
    b = dinhLyFermat(a, m, n)
    print(f"=> Output b = {b}")
