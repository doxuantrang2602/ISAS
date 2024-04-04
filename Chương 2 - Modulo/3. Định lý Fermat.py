'''
SỬ DỤNG ĐỊNH LÝ FERMAT ĐỂ TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏
Input: a = 373; m = 851; n = 6211
Tìm Output: b =
'''


def dinhLyFermat(a, m, n):
    if a >= n: # Đảm bảo a < n và n là số nguyên tố
        a = a % n
    # Áp dụng Định lý Fermat: a^(n-1) ≡ 1 (mod n)
    m = m % (n - 1) # Giảm m sử dụng phi(n) khi n là số nguyên tố: phi(n) = n - 1
    if m == 0:
        return 1
    elif m % 2 == 0:
        halfRes = dinhLyFermat(a, m // 2, n)
        return (halfRes * halfRes) % n # Chia m thành nửa và tính bình phương
    else:
        return (a * dinhLyFermat(a, m - 1, n)) % n #a*a^(m-1) mod n

if __name__ == "__main__":
    a = int(input("Nhập a = "))
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    b = dinhLyFermat(a, m, n)  # a^m mod n
    print("+> Output b =", b)
