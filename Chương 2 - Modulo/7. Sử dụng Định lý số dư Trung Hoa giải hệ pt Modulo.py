'''
SỬ DỤNG ĐỊNH LÝ SỐ DƯ TRUNG HOA ĐỂ GIẢI HỆ PHƯƠNG TRÌNH MODULO.
                    𝒙 𝒎𝒐𝒅 𝒎𝟏 = 𝒂𝟏
                    𝒙 𝒎𝒐𝒅 𝒎𝟐 = 𝒂𝟐
                    𝒙 𝒎𝒐𝒅 𝒎𝟑 = 𝒂𝟑
Input: m1 = 11; m2 = 13; m3 = 17; a1 = 6; a2 = 11; a3 = 12;
Tìm Output: x =
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

def Solve(m, a):
    M = 1
    for i in range(len(m)):
        M *= m[i]
    M_values = []
    y_values = []
    for i,mi in enumerate(m,1):
        Mi = M // mi
        yi = euclidMoRong(Mi, mi)
        M_values.append(Mi)
        y_values.append(yi)
        print(f"M{i} = {Mi}, y{i} = {yi}");
    x = 0
    for i in range(len(m)):
        x+= a[i] * y_values[i] * M_values[i]
    x %= M
    return x

if __name__ == "__main__":
    m = []
    for i in range(1,4):
        mi = int(input(f"Nhập m{i} = "))
        m.append(mi)
    a = []
    for i in range(1,4):
        ai = int(input(f"Nhập a{i} = "))
        a.append(ai)
    x = Solve(m, a)
    print(f"=> Output x = {x}")
