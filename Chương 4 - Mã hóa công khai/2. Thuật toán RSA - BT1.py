'''
Thuật toán RSA - Bài toán 1
Input: p, q, e
Output:
a) PU = {e, n} =
b) PR = {d, n} =
c) An mã: C =
d) Ba giải mã C: M’ =

Giả sử An chọn các giá trị p = 43 , q = 47 , e = 53 để tạo cặp khóa.
Hãy cho biết
a) Khóa công khai của An: PU = {e, n} =
b) cách An tạo ra khóa riêng: PR = {d, n} =
c) Cách An tạo bản mã hóa thông điệp M = 67: C =
d) Hãy cho biết cách người nhận giải mã bản mã C:
e) Việc mã hóa ở câu c) thực hiện nhiệm vụ chữ ký số hay bảo mật.
'''

from CacHamBoTro import tinhMod, euclidMoRong, phiEuler

if __name__ == "__main__":
    p = 43
    q = 47
    e = 53
    print("="*40)
    n = p * q
    phi_n = phiEuler(n)
    d = euclidMoRong(e, phi_n)

    # a) Khóa công khai PU = {e, n}
    print(f"a) Khóa công khai PU = ({e},{n})")
    # b) Khóa riêng PR = {d, n}
    print(f"b) Khóa bí mật PR = ({d}, {n})")
    print("=" * 40)

    # c) Cách An tạo bản mã hóa thông điệp M = 67:
    M = 67
    C = tinhMod(M, d, n)
    print(f"c) An mã hóa thông điệp M = {M} với C = M^d mod n = {C}")

    # d) Ba giải mã C: M’ =
    M_giai = tinhMod(C, e, n)
    print(f"d) Ba giải mã C: M' = C^e mod n = {M_giai}")
    # e) Việc mã hóa ở câu c) thực hiện nhiệm vụ chữ ký số hay bảo mật?
    print(f"e) Việc mã hóa ở câu c) thực hiện nhiệm vụ chữ ký số")


