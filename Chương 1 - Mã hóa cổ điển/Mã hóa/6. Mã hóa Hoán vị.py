'''
Input: M = NOPAINNOGAINNOPAIN
Key: K = 9
Tìm Output: C = NAOIPNANIONPNAOIGN
'''

if __name__ == "__main__":
    M = input("Nhập M = ")
    K = int(input("Nhập K = "))
    while len(M) % K != 0:
        M += 'X'  # Đảm bảo độ dài văn bản chia hết cho khóa bằng cách thêm 'X'
    C = ""
    soHang = len(M) // K
    for i in range(K):  # Duyệt qua từng cột
        for j in range(soHang):  # Duyệt qua từng hàng
            C += M[j * K + i]
    print("=> Output C = ",*C, sep="")
