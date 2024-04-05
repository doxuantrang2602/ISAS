'''
KIỂM TRA SỐ NGUYÊN A CÓ LÀ MỘT CĂN NGUYÊN THỦY CỦA SỐ NGUYÊN N?
Input: a = 3; n = 239
Tìm Output: a có là căn nguyên thủy của n không?
'''
import math

def tinhMod(a, xA, q):
    return pow(a, xA, q) # a^xA mod q

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

def ptThuaSoNguyenTo(n):
    lst = []
    p = 2
    while n > 1:
        while n % p == 0:
            lst.append(p)
            n //= p
        p += 1
    return lst

def kiemTraCanNguyenThuy(a, n):
    if math.gcd(a, n) != 1:
        return False
    phi_n = phiEuler(n)
    factors = ptThuaSoNguyenTo(phi_n) # Tìm thừa số nguyên tố của phi(n)

    # Kiểm tra a^phi(n)/p mod n != 1 cho mọi thừa số nguyên tố p của phi(n)
    for i in factors:
        if tinhMod(a, phi_n // i, n) == 1:
            return False
    return True

if __name__ == "__main__":
    a = 5
    n = 257
    if kiemTraCanNguyenThuy(a, n):
        print(f"=> {a} là căn nguyên thủy của {n}")
    else:
        print(f"=> {a} không là căn nguyên thủy của {n}")
