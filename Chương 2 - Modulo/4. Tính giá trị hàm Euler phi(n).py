'''
TÍNH GIÁ TRỊ HÀM EULER phi(n).
Input: n = 3353
Tìm Output: phi(n) =
'''
import math
def phiEuler(n):
    res = n #Khởi tạo phi(n) = n
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            res = res * (1 - 1.0/i) # Giảm phi (n)
            while n%i == 0:
                n //= i # ta loại bỏ tất cả thừa số i khỏi n
    if n > 1:
        res -= res/n
    return int(res)

if __name__ == "__main__":
    n = int(input("Nhập n = "))
    phi_n = phiEuler(n)
    print("=> Output phi(n) = {}".format(phi_n))


