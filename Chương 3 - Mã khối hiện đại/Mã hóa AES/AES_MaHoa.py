'''
PHẦN 2: MÃ HÓA
6. Tính kết quả AddRoundKey
Input: M (input) = 39400A33DB86771F578E208998CDB8A4,
       K (input) = A2E7F3E9F4EC8BB93217B94C5FD982CD
Output: state = AddRoundKey(M, K)
======================== VÒNG LẶP THỨ i, i = 1, 2, ..., 9 ===========
7. Thay thế từng byte trong state bằng bảng S-box SubByte
Input: state (kết quả bài 6 cho lần lặp 1 hoặc kết quả bài 10 cho lần lặp kế tiếp) = ,
    Sbox
Output: state = SubByte (state)
8. Dịch vòng trái các byte trong state ShiftRows
Input: state (kết quả bài 7) = ,
Output: state = ShiftRows (state)
9. Trộn các byte trong state MixColumns
Input: state (kết quả bài 8) = ,
Output: state = MixColumns (state)
10. Dịch vòng trái các byte trong state AddRoundKey
Input: state (kết quả bài 9) = ,
Ki (kết quả bài 5) =
Output: state = AddRoundKey (state, Ki)
'''
from AES_SinhKhoa import *

def hexToMatrix(hexStr):
    maTran = []
    for _ in range(4):
        hang = []
        for _ in range(4):
            hang.append('00')
        maTran.append(hang)
    for i in range(4):
        for j in range(4):
            maTran[j][i] = hexStr[i*8 + j*2 : i*8 + j*2 + 2]
    return maTran

def XORBYTE(byte1, byte2):
    return hex(int(byte1, 16) ^ int(byte2, 16))[2:].zfill(2).upper()

def ADDROUNDKEY(M, K):
    maTranM = hexToMatrix(M)
    maTranK = hexToMatrix(K)
    state = []
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append('00')
        state.append(row)
    for i in range(4):
        for j in range(4):
            state[i][j] = XORBYTE(maTranM[i][j], maTranK[i][j])
    return state

def SUBBYTE(state):
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            state[i][j] = Sbox[byte.upper()]
    return state

def SHIFTROW(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]
    return state

def nhanMaTran(a, b):
    if b == 0x01:
        return a
    elif b == 0x02:
        if a & 0x80:
            return ((a << 1) & 0xFF) ^ 0x1B
        else:
            return (a << 1) & 0xFF
    elif b == 0x03:
        return nhanMaTran(a, 0x02) ^ a

def MIXCOLUMN(state):
    maTranMix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]
    maTranKq = []
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append('00')
        maTranKq.append(row)
    for i in range(4):
        for j in range(4):
            res = 0
            for k in range(4):
                res ^= nhanMaTran(int(state[k][j], 16), maTranMix[i][k])
            maTranKq[i][j] = format(res, '02x').upper()
    return maTranKq

if __name__ == "__main__":
    M = "39400A33DB86771F578E208998CDB8A4"
    K = "A2E7F3E9F4EC8BB93217B94C5FD982CD"
    stateADD = ADDROUNDKEY(M, K)
    print("Kết quả của AddRoundKey:")
    for row in stateADD:
        print(*row)

    stateSUB = SUBBYTE(stateADD)
    print("Kết quả của SubByte:")
    for row in stateSUB:
        print(' '.join(row))

    stateSHIFT = SHIFTROW(stateSUB)
    print("Kết quả của ShiftRows:")
    for row in stateSHIFT:
        print(' '.join(row))

    stateMIX = MIXCOLUMN(stateSHIFT)
    print("Kết quả của MixColumns:")
    for row in stateMIX:
        print(' '.join(row))