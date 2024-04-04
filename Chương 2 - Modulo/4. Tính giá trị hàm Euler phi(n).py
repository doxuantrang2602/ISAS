'''
TÍNH GIÁ TRỊ HÀM EULER phi(n).
Input: n = 3353
Tìm Output: phi(n) =
'''


def phiEuler(n):
    res = n  # Khởi tạo phi(n) bằng n
    p = 2  # Bắt đầu với số nguyên tố nhỏ nhất

    # Kiểm tra mọi số nguyên tố p cho đến căn bậc hai của n
    while p * p <= n:
        # Nếu p là ước số của n
        if n % p == 0:
            # Trừ đi tất cả các ước số p
            while n % p == 0:
                n //= p
            res -= res // p
        p += 1

    # Nếu n còn lại là một số nguyên tố lớn hơn 1
    if n > 1:
        res -= res // n

    return res

if __name__ == "__main__":
    n = 3353
    res = phiEuler(n)
    print(f"phi({n}) = {res}")
