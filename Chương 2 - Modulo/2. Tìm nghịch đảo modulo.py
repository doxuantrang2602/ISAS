'''
TÌM NGHỊCH ĐẢO 𝒙 = 𝒂^−𝟏 𝒎𝒐𝒅 𝒏 THEO ĐỊNH NGHĨA VÀ THUẬT TOÁN EUCLID – MỞ RỘNG
Input: a = 3122; n = 3593
Tìm Output: x =
'''
def euclidMoRong(a, n):
    print(f"| {'r':>5} | {'q':>5} | {'x':>5} | {'y':>5}")  # In tiêu đề cột
    print("-"*32)
    r1, r2 = n, a
    x1, x2 = 1, 0
    y1, y2 = 0, 1

    # In giá trị ban đầu của r1, q, x1, y1
    print(f"| {r1:>5} | {'':>5} | {x1:>5} | {y1:>5}")
    print(f"| {r2:>5} | {'':>5} | {x2:>5} | {y2:>5}")
    print("-" * 32)

    while r2 != 0:
        q = r1 // r2  # Tính thương
        r1, r2 = r2, r1 - q * r2  # Cập nhật r
        x1, x2 = x2, x1 - q * x2  # Cập nhật x
        y1, y2 = y2, y1 - q * y2  # Cập nhật y
        print(f"| {r2:>5} | {q:>5} | {x2:>5} | {y2:>5}")
    res = 0
    if r1 == 1:
        res = y1
    else: res = None
    # Nếu res là số âm
    if res is not None and res < 0:
        res += n
    return res

if __name__ == "__main__":
    a = int(input("Nhập a = "))
    n = int(input("Nhập n = "))
    res = euclidMoRong(a, n)
    if res is not None:
        print(f"=> Output C = {res}")
    else:
        print("=> Không tìm thấy Output C thỏa mãn !")
