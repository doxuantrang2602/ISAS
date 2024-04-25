'''
KIỂM TRA SỐ NGUYÊN A CÓ LÀ MỘT CĂN NGUYÊN THỦY CỦA SỐ NGUYÊN N?
Input: a = 3; n = 239
Tìm Output: a có là căn nguyên thủy của n không?
'''
from CacHamBoTro import ptThuaSoNguyenTo, phiEuler
import math

def kiemTraCanNguyenThuy(a, n):
    if math.gcd(a, n) != 1:
        return False
    phi_n = phiEuler(n)
    factors = ptThuaSoNguyenTo(phi_n)
    for x in factors:
        if pow(a, phi_n // x, n) == 1:
            return False
    return True

if __name__ == "__main__":
    a = 3
    n = 239
    if kiemTraCanNguyenThuy(a, n):
        print(f"=> {a} là căn nguyên thủy của {n}")
    else:
        print(f"=> {a} không là căn nguyên thủy của {n}")
