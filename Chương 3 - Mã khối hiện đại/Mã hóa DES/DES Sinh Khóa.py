PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

def hexToBin(s):
    strBin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    res = ""
    for c in s.upper():
        res += strBin[c]
    return res

def hoanVi(k, arr, n):
    s = ""
    for i in range(n):
        s += k[arr[i] - 1]
    return s

def dichVongTrai(k, i):
    shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    bitRotated = shift[i] # Dịch vòng trái chuỗi k dựa trên số lần dịch bitRotated
    return k[bitRotated:] + k[:bitRotated] # k[s:] lấy phần kí tự từ s trở đi

if __name__ == "__main__":
    K = "03756CD378146EC7"
    K = hexToBin(K)
    # Bước 1: Tính C0 và D0
    K0 = hoanVi(K, PC1, 56)
    C0, D0 = K0[:28], K0[28:]

    # Bước 2 và 3: Tính Ci, Di và ki
    keys = []
    Ci, Di = C0, D0
    for i in range(16):
        Ci = dichVongTrai(Ci, i)
        Di = dichVongTrai(Di, i)
        CiDi = Ci + Di
        Ki = hoanVi(CiDi, PC2, 48)
        keys.append(Ki)
    for i, key in enumerate(keys,1):
        print(f"K{i} = {key}")