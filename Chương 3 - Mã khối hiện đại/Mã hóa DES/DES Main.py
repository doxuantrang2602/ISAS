from  DES_MaHoa import *
from DES_SinhKhoa import *
'''
K = 03756CD378146EC7
M = 66581B2AE5B0BD6D
'''
IP1_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
def IP_1(x):
    C=[]
    for i in IP1_table:
        C.append(x[i-1])
    return ''.join(C)
def DES(x,k):
    ### Sinh Khoá
    # chuyển k về hệ 2
    k= hexToBin(k)
    #hoán vị PC1
    pc1= PC1(k)
    C0,D0= SPLIT_KEY(pc1)
    C,D=[],[]
    C.append(C0)
    D.append(D0)
    # dịch vòng
    bit_rotated = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i,j in enumerate(bit_rotated):
        C.append(Shift_Left(C[i],j))
        D.append(Shift_Left(D[i], j))
    C= C[1:]
    D=D[1:]
    # PC2 -> 16 khóa
    K = []
    for i in range(0, 16):
        K.append(PC2(C[i], D[i]))
    ### Mã hóa
    # hoán vị IP
    x= hexToBin(x)
    ip= IP(x)
    L0, R0 = SPLIT_KEY(ip)
    L, R = [], []
    L.append(L0)
    R.append(R0)
    ## 16 Vòng lặp (Mã hóa)
    for i in range(16):
        er = E(R[i])
        xor = XOR(er, K[i])
        s_box = SUB(xor)
        f = P(s_box)
        kq = XOR(L[i], f)
        L.append(R[i])
        R.append(kq)
    # 32bit swap
    M = R[-1] + L[-1]
    #hoán vị IP_1
    ip_1 = IP_1(M)
    # chuyển hệ 2 -> hệ 16
    bin_to_hex = hex(int(ip_1, 2))
    C=bin_to_hex[2:].upper()

    return C

if __name__ == '__main__':
    k= input("Nhập k: ")
    x=input("Nhập x: ")
    print("Kết quả: ",DES(x,k))

