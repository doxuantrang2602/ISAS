'''
CHỮ KÝ ĐIỆN TỬ DSA
Input: H(M), p , q , h, xA , k
Output:
a) Khóa công khai yA =
b) Chữ ký số (r, s) =
c) Ba xác minh chữ ký số?

Giả sử An cần gửi cho Ba một bản tin M kèm chữ ký số, bản tin M có mã băm là H(M) =
An và Ba thống nhất các giá trị: p = 89, q = 11, h = 38
và An chọn xA = 5, k = 2
Hãy cho biết
a) Khóa công khai của An: yA =
b) Chữ ký số của An cho bản tin M: (r, s) =
c) Cách Ba xác minh chữ ký số được đính kèm với bản tin M?
'''
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

if __name__ == "__main__":
    H_M = 7
    p = 89
    q = 11
    h = 38
    xA = 5
    k = 2
    g = pow(h, (p - 1) // q, p)
    # a) Khóa công khai yA và
    yA = tinhMod(g, xA, p)
    print(f"a) Khóa công khai yA = {yA}")

    # b) Chữ ký số (r, s)
    r = tinhMod(g, k, p) % q
    s = (euclidMoRong(k, q) * ((H_M + xA * r) % q)) % q
    print(f"b) Chữ ký số (r, s) = ({r}, {s})")

    # c) Ba xác minh chữ ký số
    w = euclidMoRong(s, q)
    u1 = (H_M * w) % q
    u2 = (r * w) % q
    v = ((tinhMod(g, u1, p) * tinhMod(yA, u2, p)) % p) % q
    if v == r:
        print(f"c) Chữ kí đúng !")
    else:
        print(f"Chữ kí không hợp lệ !")



