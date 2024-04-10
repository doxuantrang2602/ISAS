'''
Sinh khóa
1. Viết hàm K1 = PC1(K) thực hiện hoán vị PC1
Input: K - chuỗi số 64 bit
Output: K1 – chuỗi số 56 bit là hoán vị của K theo ma trận PC1
2. Viết hàm SPLIT_KEY(K1, C, D) tách chuỗi số 56 bit (K1) thành 2 nửa 28 bit trái (C) và phải (D);
Input: K1 – chuỗi số 56 bit
Output: C, D – chuỗi số 28 bit
3. Viết hàm ShiftLeft(x, s) dịch vòng trái s bit đối với chuỗi số 28 bit (x)
Input: x – chuỗi số 28 bit, s – số nguyên dương <28
Output: x – chuỗi số 28 bit đã dịch vòng trái s bit
4. Viết hàm Ks = PC2(C, D, s) thực hiện hoán vị PC2
Input: C, D - chuỗi số 28 bit, s – số nguyên dương < 28
Output: Ks – chuỗi số 48 bit là hoán vị của C, D theo ma trận PC2.
'''

shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def hexToBin(s):
    strBin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    bin = ""
    for c in s.upper():
        bin += strBin[c]
    return bin

def PC1(K):
    PC1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    K1 = ""
    for x in PC1_table:
        K1 += K[x-1]
    return K1

def SPLIT_KEY(K1):
    m = len(K1) // 2
    C = K1[:m]
    D = K1[m:]
    return C, D

def ShiftLeft(x, s):
    bitRotated = shift[s]
    return x[bitRotated:] + x[:bitRotated]

def PC2(C,D):
    PC2_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    K= C+D
    K1 = ""
    for x in PC2_table:
        K1+= K[x-1]
    return K1

if __name__ == '__main__':
    K = "03756CD378146EC7"
    K = hexToBin(K)
    K0 = PC1(K)
    print("=> Hoán vị PC1: ",K0, sep="")
    C0,D0= SPLIT_KEY(K0)
    print(f"C0 = {C0}")
    print(f"D0 = {D0}")
    C1=ShiftLeft(C0, 1)
    D1=ShiftLeft(D0, 1)
    print(f"Dịch vòng trái 1 bit của C0 = C1 = {C1}")
    print(f"Dịch vòng trái 1 bit của D0 = D1 = {D1}")
    K1 = PC2(C1,D1)
    print(f"=> Hoán vị PC2(C1D1) = {K1} ")
