'''
Input: M = NOPAINNOGAINNOPAIN
Key: K = 9
Tìm Output: C = NAOIPNANIONPNAOIGN
'''

if __name__ == "__main__":
    M = input("Nhập M = ")
    K = int(input("Nhập K = "))
    M = M.replace(" ", "").upper()
    while len(M) % K != 0:
        M += 'X'  # Đảm bảo độ dài văn bản chia hết cho khóa bằng cách thêm 'X'
    # Tạo bảng hoán vị
    maTran = []
    for i in range(0, len(M), K):
        maTran.append(M[i:i + K])
    # Đọc văn bản đã mã hóa theo cột
    C = []
    for i in range(K):  # Duyệt qua từng cột
        for row in maTran:  # Duyệt qua từng hàng
            C.append(row[i])
    print("=> Output C = ",*C, sep="")
