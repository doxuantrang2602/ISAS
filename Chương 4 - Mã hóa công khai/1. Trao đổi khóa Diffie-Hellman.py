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

from CacHamBoTro import tinhLuyThuaModulo

if __name__ == "__main__":
    q = 6199
    a = 3
    xA = 531
    xB = 540
    print("="*25)

    #Tính khóa công khai yA và KA
    yA = tinhLuyThuaModulo(a, xA, q) # yA = a^xA (mod q)
    yB = tinhLuyThuaModulo(a, xB, q) # yB = a^xB (mod q)
    print(f"Khóa công khai yA = {yA}")
    print(f"Khóa công khai yB = {yB}")
    print("=" * 25)
    # Tính khóa chung
    KA = tinhLuyThuaModulo(yB, xA, q)
    KB = tinhLuyThuaModulo(yA, xB, q)

    if KA == KB:
        print("=> Trao đổi khóa thành công ")
        print("=> Khóa chung K = ", KA)
    else:
        print("Có lỗi trong quá trình trao đổi khóa.")

