def hex_to_bin(s):
    hex_to_bin= {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    K=""
    for c in s.upper():
        K+= hex_to_bin[c]
    return K

def PC1(K):
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    K1=[]
    for x in pc1_table:
        K1.append(K[x-1])
    return K1
def SPLIT(K):
    m= len(K)//2
    C= K[:m]
    D=K[m:]
    return C,D
def Shift_Left(x,s): #x- chuỗi, s- số bit dịch
    list_x= list(x)
    x_shift_left= list_x[s:]+ list_x[:s]
    return ''.join(x_shift_left)
def PC2(C,D):
    pc2_table = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    K= C+D
    K1=[]
    for x in pc2_table:
        K1.append(K[x-1])
    return K1

if __name__ == '__main__':
    K= '03756CD378146EC7'
    K= hex_to_bin(K)
    K1= ''.join(PC1(K))
    print("Hoán vị PC1: ",K1, sep="")
    C,D= SPLIT(K1)
    print("C= ",C)
    print("D= ",D)
    C=Shift_Left(C,1)
    D=Shift_Left(D, 1)
    print("Shift Left 1 bit của C= ", C)
    print("Shift Left 1 bit của D= ", D)

    Ks= ''.join(PC2(C,D))
    print("Hoán vị PC2: ", Ks)

