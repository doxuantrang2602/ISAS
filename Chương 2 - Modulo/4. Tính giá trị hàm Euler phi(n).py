'''
TÍNH GIÁ TRỊ HÀM EULER phi(n).
Input: n = 3353
Tìm Output: phi(n) =
'''
from CacHamBoTro import ptThuaSoNguyenTo

def phiEuler(n):
    factors = ptThuaSoNguyenTo(n)
    res = n
    for p in factors:
        res *= (1 - 1.0/p)
    return int(res)

if __name__ == "__main__":
    n = 3353
    phi_n = phiEuler(n)
    print(f"=> Output phi(n) = {phi_n}")

