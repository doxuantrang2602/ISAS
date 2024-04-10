'''
Giả sử An và Ba trao đổi bằng hệ mật mã ElGamal, có các giá trị chung là
q = 7001 là một số nguyên tố, a = 6 là căn nguyên thủy của q.
An chọn khóa riêng là xA = 382
Hãy cho biết
a) Khóa công khai của An: PU = {q, a, YA} với yA =
b) Ba chọn số k = 589 để mã hóa bản tin M = 442 gửi cho An. Bản mã là (C1, C2) =
c) Cách An giải bản mã (C1, C2)?
'''

def euclidMoRong(a, n):
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    if r1 == 1:
        res = y1
    else:
        res = None
    if res is not None and res < 0:
        res += n
    return res

if __name__ == "__main__":
    q = 7001
    a = 6
    xA = 382

    yA = pow(a,xA, q)
    print(f"a) Khóa công khai PU = {{q,a,yA}} = {{{q},{a},{yA}}}")
    print("="*50)

    k = 589
    M = 442
    K = pow(yA, k, q)
    C1 = pow(a, k, q)
    C2 = pow(K*M, 1, q)
    print(f"b) Bản mã (C1, C2) là: ({C1}, {C2})")
    print("=" * 50)

    K_giaiMa = pow(C1, xA, q)
    M_giaiMa = (C2%q * euclidMoRong(K_giaiMa,q)) % q
    print(f"c) An giải bản mã (C1, C2) được K = {K_giaiMa}, M = {M_giaiMa}")
