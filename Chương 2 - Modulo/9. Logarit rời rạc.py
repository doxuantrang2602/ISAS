'''
Đề bài: TÌM LOGARITHM RỜI RẠC CỦA SỐ b VỚI CƠ SỐ a (mod n), 𝒌 = 𝐥𝐨𝐠𝒂 𝒃 (𝒎𝒐𝒅 𝒏).
Input: a = 6; b = 5; n = 13
=> Tìm Output: k =
'''
if __name__ == "__main__":
    a = 6
    b = 5
    n = 13
    res = 0
    kt = False
    for i in range(n):
        if pow(a, i, n) == b:
           res = i
           kt = True
           break
    if kt == True:
        print(f"log{a} {b} (mod {n}) = {res}")
    else:
        print("Không có giá trị !")
