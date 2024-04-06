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
import math

def tinhMod(a, xA, q):
    return pow(a, xA, q) # a^xA mod q

def euclidMoRong(a, n):
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while r2 != 0:
        q = r1 // r2  # Tính thương
        r1, r2 = r2, r1 - q * r2  # Cập nhật r
        x1, x2 = x2, x1 - q * x2  # Cập nhật x
        y1, y2 = y2, y1 - q * y2  # Cập nhật y
    if r1 == 1:
        res = y1
    else: res = None
    # Nếu res là số âm
    if res is not None and res < 0:
        res += n
    return res

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

if __name__ == "__main__":
    p = int(input("Nhập p = "))
    q = int(input("Nhập q = "))
    e = int(input("Nhập e = "))
    print("="*20)
    n = p * q
    phi_n = phiEuler(n)
    d = euclidMoRong(e, phi_n)

    # a) Khóa công khai PU = {e, n}
    print(f"a) Khóa công khai PU = ({e},{n})")
    # b) Khóa riêng PR = {d, n}
    print(f"b) Khóa bí mật PR = ({d}, {n})")
    print("=" * 20)

    # c) Cách An tạo bản mã hóa thông điệp M = 67:
    M = int(input("Nhập thông điệp M = "))
    C = tinhMod(M, d, n)
    print(f"c) An mã hóa thông điệp M = {M} với C = M^d mod n = {C}")

    # d) Ba giải mã C: M’ =
    M_giai = tinhMod(C, e, n)
    print(f"d) Ba giải mã C: M' = C^e mod n = {M_giai}")
    # e) Việc mã hóa ở câu c) thực hiện nhiệm vụ chữ ký số hay bảo mật?
    print(f"e) Việc mã hóa ở câu c) thực hiện nhiệm vụ chữ ký số")


