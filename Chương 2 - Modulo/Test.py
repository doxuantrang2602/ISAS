def euclidMoRong(n, a):
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    if r1 == 1:
        return y1 if y1 > 0 else y1 + n
    else:
        return None

def ptThuaSoNguyenTo(n):
    s = set()
    p = 2
    while n > 1:
        while n % p == 0:
            s.add(p)
            n //= p
        p += 1
    return s

def dinhLyPhanDuTrungHoa(a, k, n):
    print("a = {}, k = {}, n = {}".format(a, k, n))
    # Bước 1: Phân tích n thành tích của các số nguyên tố cùng nhau
    fac = ptThuaSoNguyenTo(n)
    print("m1,m2,...,mk", fac)

    # Bước 2: Tính Mi = M / mi cho mỗi i và ci = Mi*(Mi^(-1) mod mi)
    M = n  # M là tích của tất cả các m_i, ở đây chính là n
    print("Tính Mi và ci:")
    M_values = []
    c_values = []
    for mi in fac:
        Mi = M // mi
        ci = euclidMoRong(mi, Mi)
        M_values.append(Mi)
        c_values.append(ci)
        print(f"Mi = {Mi}, ci = {ci}")

    # Bước 3: Tính ai = a^k mod mi cho mỗi i
    a_values = [pow(a, k, mi) for mi in fac]
    print("Tính ai = a^k mod mi:")
    for i, ai in enumerate(a_values):
        print(f"a{i + 1} = {ai}")

    # Bước 4: Tính A = Σ(ai * ci * Mi) mod M (i->k)
    A = 0
    for i in range(len(fac)):
        A += a_values[i] * c_values[i] * M_values[i]
    A %= n
    print("Tính A = Σ(ai * ci * Mi) mod M:")
    print("A = ",A)
    return A