'''
1. TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏 BẰNG CÁCH HẠ BẬC LŨY THỪA
Input: a = 449; m = 6763; n = 6763
Tìm Output: b =
'''

def tinhLuyThuaModulo(a, m, n):
    res = 1 # Khởi tạo kết quả
    a = a % n # Chuyển a thành a mod n
    while m > 0:
        if m % 2 == 1:
            res = (res * a) % n  # Nếu m là số lẻ, nhân b với a
        m = m // 2 # Hạ bậc lũy thừa m
        a = (a * a) % n  # Cập nhật a
    return res
if __name__ == "__main__":
    a = int(input("Nhập a = "))
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    b = tinhLuyThuaModulo(a, m, n)
    print(f"=> Output b = {b}")
