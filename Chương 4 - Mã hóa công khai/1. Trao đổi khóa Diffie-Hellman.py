'''
Trao đổi khóa Diffie-Hellman
Input: số nguyên tố q, a (căn nguyên thủy của q), xA = xB =
Ouput: yA, yB, K

Đề bài bài tập:
Giả sử An và Ba muốn trao đổi khoá phiên, họ đồng ý chọn số nguyên tố q = 6199
và a = 3 (là căn nguyên thủy của q).
An chọn khóa riêng xA = 531
Ba chọn khóa riêng xB = 540
Hãy cho biết
a) Cách An tính ra khóa công khai yA và khóa phiên K? yA = K =
b) Cách Ba tính ra khóa công khai yB và khóa phiên K? yB = K =
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
    q = int(input("Nhập q = "))
    a = int(input("Nhập a = "))
    xA = int(input("Nhập xA = "))
    xB = int(input("Nhập xB = "))
    print("="*20)

    #Tính khóa công khai yA và KA
    yA = tinhLuyThuaModulo(a, xA, q) # yA = a^xA (mod q)
    yB = tinhLuyThuaModulo(a, xB, q) # yB = a^xB (mod q)
    print(f"Khóa công khai yA = {yA}")
    print(f"Khóa công khai yB = {yB}")
    print("=" * 20)
    # Tính khóa chung
    KA = tinhLuyThuaModulo(yB, xA, q)
    KB = tinhLuyThuaModulo(yA, xB, q)

    if KA == KB:
        print("=> Trao đổi khóa thành công ")
        print("=> Khóa chung K = ", KA)
    else:
        print("Có lỗi trong quá trình trao đổi khóa.")

