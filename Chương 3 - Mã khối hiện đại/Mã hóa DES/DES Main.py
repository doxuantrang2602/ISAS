'''
Mã hóa DES – xây dựng hàm y = DES (x, k) thực hiện mã hóa theo thuật toán DES
input: x, k – chuỗi số 64 bit
Output: y – chuỗi số 64 bít được mã hóa từ x theo thuật toán DES với khóa k
'''
from DES_MaHoa import *

def FP(x):
    FP_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    res = ""
    for i in FP_table:
        res += x[i-1]
    return res

def DES(x, k):
    K = hexToBin(k)
    M = hexToBin(x)
    K1 = PC1(K)
    C, D = SPLIT_KEY(K1)
    Ks = []
    for i in range(16):
       C = ShiftLeft(C, shift[i])
       D = ShiftLeft(D, shift[i])
       Ks.append(PC2(C,D))
       print(f"Khóa {i+1} = {Ks[i]}")
    IP_M = IP(M)
    L0, R0 = SPLIT_KEY(IP_M)
    L, R = [], []
    L.append(L0)
    R.append(R0)
    print(f"Vòng 0: L = {L0}, R = {R0}")
    for i in range(16):
        ER = E(R[i])
        A = XOR(ER, Ks[i])
        B = SUB(A)
        F = P(B)
        R_res = XOR(F, L[i])
        L.append(R[i])
        R.append(R_res)
        print(f"Vòng {i+1}: L = {L[i+1]}, R = {R[i+1]}")
    y = FP(R[16]+L[16])
    return y
def binToHex(s):
    strHex = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex = ""
    for i in range(0, len(s), 4):
        hex += strHex[s[i:i+4]]
    return hex

if __name__ == '__main__':
    K = "03756CD378146EC7"
    M = "66581B2AE5B0BD6D"
    resDes = DES(M, K)
    print(f"=> Kết quả mã hóa Des: {resDes}")
    print(f"=> Mã Hex: {binToHex(resDes)}")

'''
K = 03756CD378146EC7
M = 66581B2AE5B0BD6D
Output: F20CA5AE288E3903
'''