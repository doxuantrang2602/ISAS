'''
Input: M = NOPAINNOGAINNOPAIN
Key: K = 9
Tìm Output: C =
'''

def maHoaHoanVi(text, key):
    text = text.replace(" ", "").upper() # Bỏ qua khoảng trắng và chuyển văn bản thành chữ hoa
    while len(text) % key != 0:
        text += 'X'  # Đảm bảo độ dài văn bản chia hết cho khóa bằng cách thêm 'X'

    # Tạo bảng hoán vị
    for i in range(0, len(text), key):
        maTran = text[i:i + key]

    # Đọc văn bản đã mã hóa theo cột
    res =""
    for i in range(key):  # Duyệt qua từng cột
        for row in maTran:  # Duyệt qua từng hàng
            res += row[i]
    return res

if __name__ == "__main__":
    M = input("Nhập M = ")
    K = int(input("Nhập K = "))
    C = maHoaHoanVi(M, K)
    print("=> Output C =", C)

