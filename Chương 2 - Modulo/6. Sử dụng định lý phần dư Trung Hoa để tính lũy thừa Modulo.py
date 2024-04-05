'''
SỬ DỤNG ĐỊNH LÝ SỐ DƯ TRUNG HOA ĐỂ TÍNH LŨY THỪA modulo 𝒃 = 𝒂^𝒌 𝒎𝒐𝒅 𝒏
Input: a = 113; k = 58; n = 37259
Tìm Output: b =
'''

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

def ptThuaSoNguyenTo(n):
    lst = []
    p = 2
    while n > 1:
        while n % p == 0:
            lst.append(p)
            n //= p
        p += 1
    return lst

def dinhLyPhanDuTrungHoa(a, k, n):
    print("Input:")
    print(f"a = {a}; k = {k}; n = {n}")

    # Bước 1: Phân tích n thành tích của các số nguyên tố cùng nhau từng đôi một
    factors = ptThuaSoNguyenTo(n)

    print("Phân tích n thành tích các số nguyên tố cùng nhau:")
    print("m1, m2, ..., mk =", factors)

    # Bước 2: Tính M
    M = n  # M là tích của tất cả các m_i, ở đây chính là n

    # Bước 3: Tính Mi = M / mi cho mỗi i và ci = Mi^(-1) mod mi
    print("Tính Mi và ci:")
    M_values = []
    c_values = []
    for i,m in enumerate(factors,1):
        Mi = M // m
        ci = Mi*euclidMoRong(Mi, m)
        M_values.append(Mi)
        c_values.append(ci)
        print(f"M{i} = {Mi}, c{i} = {ci}")

    # Bước 4: Tính ai = a^k mod mi cho mỗi i
    a_values = []
    for mi in factors:
        a_values.append(pow(a, k, mi))

    print("Tính ai = a^k mod mi:")
    for i, x in enumerate(a_values,1):
        print(f"a{i} = {x}")

    # Bước 5: Tính A = Σ(ai * ci * Mi) mod M
    A = 0
    for i in range(len(factors)):
        A += a_values[i] * c_values[i] * M_values[i]
    A %= n

    print("Tính A = Σ(ai * ci * Mi) mod M:")
    print("A =", A)

    return A
if __name__ == "__main__":
    a = 113
    k = 58
    n = 37259
    b = dinhLyPhanDuTrungHoa(a, k, n)
    print("=> Output b =", b)