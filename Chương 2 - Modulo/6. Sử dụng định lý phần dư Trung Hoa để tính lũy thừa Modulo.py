'''
SỬ DỤNG ĐỊNH LÝ SỐ DƯ TRUNG HOA ĐỂ TÍNH LŨY THỪA modulo 𝒃 = 𝒂^𝒌 𝒎𝒐𝒅 𝒏
Input: a = 113; k = 58; n = 37259
Tìm Output: b =
'''

def extended_gcd(a, b):
    # Tìm số nguyên x, y sao cho ax + by = gcd(a, b)
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def modular_inverse(a, m):
    # Tìm nghịch đảo modulo của a trong modulo m
    d, x, y = extended_gcd(a, m)
    if d != 1:
        raise ValueError("a không có nghịch đảo modulo trong modulo m")
    return x % m

def dinhLyPhanDuTrungHoa(a, k, n):
    print("Input:")
    print(f"a = {a}; k = {k}; n = {n}")

    # Bước 1: Phân tích n thành tích của các số nguyên tố cùng nhau từng đôi một
    factors = []
    temp_n = n
    i = 2
    while temp_n > 1:
        if temp_n % i == 0:
            factors.append(i)
            while temp_n % i == 0:
                temp_n //= i
        i += 1

    print("Phân tích n thành tích các số nguyên tố cùng nhau:")
    print("m1, m2, ..., mk =", factors)

    # Bước 2: Tính M
    M = n  # M là tích của tất cả các m_i, ở đây chính là n

    # Bước 3: Tính Mi = M / mi cho mỗi i và ci = Mi^(-1) mod mi
    print("Tính Mi và ci:")
    M_values = []
    c_values = []
    for mi in factors:
        Mi = M // mi
        ci = modular_inverse(Mi, mi)
        M_values.append(Mi)
        c_values.append(ci)
        print(f"Mi = {Mi}, ci = {ci}")

    # Bước 4: Tính ai = a^k mod mi cho mỗi i
    a_values = [pow(a, k, mi) for mi in factors]

    print("Tính ai = a^k mod mi:")
    for i, ai in enumerate(a_values):
        print(f"a{i + 1} = {ai}")

    # Bước 5: Tính A = Σ(ai * ci * Mi) mod M
    A = sum(ai * ci * Mi for ai, ci, Mi in zip(a_values, c_values, M_values)) % M

    print("Tính A = Σ(ai * ci * Mi) mod M:")
    print("A =", A)

    return A
if __name__ == "__main__":
    a = 113
    k = 58
    n = 37259
    b = dinhLyPhanDuTrungHoa(a, k, n)
    print("=> Output b =", b)

