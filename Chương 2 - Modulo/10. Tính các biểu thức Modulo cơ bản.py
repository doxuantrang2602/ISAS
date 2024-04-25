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

from CacHamBoTro import tinhLuyThuaModulo, euclidMoRong

if __name__ == "__main__":
    a, b, x, y, n = 43, 53, 308, 455, 179

    # Tính các biểu thức modulo
    A1 = (tinhLuyThuaModulo(a, x, n) + tinhLuyThuaModulo(b, y, n)) % n
    A2 = (tinhLuyThuaModulo(a, x, n) - tinhLuyThuaModulo(b, y, n)) % n
    A3 = (tinhLuyThuaModulo(a, x, n) * tinhLuyThuaModulo(b, y, n)) % n
    A4 = euclidMoRong(tinhLuyThuaModulo(b, y, n), n)
    A5 = (tinhLuyThuaModulo(a, x, n) * euclidMoRong(tinhLuyThuaModulo(b, y, n), n)) % n

    print(f"=> A1 = {A1}")
    print(f"=> A2 = {A2}")
    print(f"=> A3 = {A3}")
    print(f"=> A4 = {A4}")
    print(f"=> A5 = {A5}")
