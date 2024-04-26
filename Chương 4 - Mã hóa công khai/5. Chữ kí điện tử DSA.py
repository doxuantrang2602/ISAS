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
from CacHamBoTro import tinhMod, euclidMoRong

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



