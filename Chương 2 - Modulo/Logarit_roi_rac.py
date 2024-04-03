'''
Đề bài: TÌM LOGARITHM RỜI RẠC CỦA SỐ b VỚI CƠ SỐ a (mod n), 𝒌 = 𝐥𝐨𝐠𝒂 𝒃 (𝒎𝒐𝒅 𝒏).
Input: a = 6; b = 5; n = 13
=> Tìm Output: k =
'''

import math
def Tinh_Mod(a, i, n):
    return pow(a,i,n) # Tính a^i mod n

def euler_Phi(n):
    res = 0 # Biến res để đếm số lượng nguyên tố cùng nhau với n
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            res += 1 # Nếu i và n nguyên tố cùng nhau thì tăng res lên 1
    return res

def logaritRoiRac(a, b, n):
    print("=========")
    print("| i | p |")
    print("=========")
    for i in range(1, euler_Phi(n)):
        p = Tinh_Mod(a, i, n)
        print(f"|{i:<3}|{p:<3}|")
        if p == b: # Kiểm tra xem a^i mod n có bằng b không => loga b (mod n)=i
            print("=> log{} {} (mod {}) = {}".format(a,b,n,i))
            break
    else:
        print("Khong ton tai")

if __name__ == "__main__":
    a = int(input("Nhập a = "))
    b = int(input("Nhập b = "))
    n = int(input("Nhập n = "))
    logaritRoiRac(a,b,n)


