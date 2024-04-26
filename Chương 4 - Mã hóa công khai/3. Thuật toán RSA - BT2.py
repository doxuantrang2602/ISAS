'''
Thuật toán RSA - Bài toán 2:
Input: p, q, e
Output:
a) PU = {e, n} =
b) PR = {d, n} =
c) Ba mã: C =
d) An giải mã C: M’ =
'''
from CacHamBoTro import tinhMod, euclidMoRong, phiEuler

if __name__ == "__main__":
    p = 43
    q = 47
    e = 53
    print("=" * 40)
    n = p * q
    phi_n = phiEuler(n)
    d = euclidMoRong(e, phi_n)

    # a) Khóa công khai PU = {e, n}
    print(f"a) Khóa công khai PU = ({e},{n})")
    # b) Khóa riêng PR = {d, n}
    print(f"b) Khóa bí mật PR = ({d}, {n})")
    print("=" * 40)

    # c) Ba Mã hóa gửi cho An
    M = 67
    C = tinhMod(M,e,n)
    print(f"c) Ba mã hóa thông điệp M = {M} với C = M^e mod n = {C}")

    # d) An giải mã
    M_giai = tinhMod(C, d, n)
    print(f"d) An giải mã C: M' = {M_giai}")

