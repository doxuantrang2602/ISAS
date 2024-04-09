'''
Mã hóa
1. Viết hàm y = SUBBYTE(state) thực hiện việc thế byte.
Input: state – ma trận 4x4 = 16 byte
Output: y – ma trận 4x4 = 16 byte byte là kết quả thay thế byte x theo bảng S-box
2. Viết hàm y = SHIFTROW(state) thực hiện việc dịch hàng.
Input: state – ma trận 4x4 = 16 byte
Output: y – ma trận 4x4 = 16 byte byte là kết quả dịch hàng.
3. Viết hàm y = MIXCOLUMN(state) thực hiện việc nhân ma trận.
Input: state – ma trận 4x4 = 16 byte
Output: y – ma trận 4x4 = 16 byte byte là kết quả mixcolumn của state
4. Viết hàm y = ADDROUNDKEY(state, K) thực hiện việc nhân ma trận.
Input: state, K – ma trận 4x4 = 16 byte
Output: y – ma trận 4x4 = 16 byte byte là kết quả AddRoundKey của state và khóa K
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

def changeState(state):
    newState = []
    for i in range(4):
        rc = []
        for j in range(4):
            rc.append(state[j][i])
        newState.append(rc)
    return newState

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
    for i in range(4):
        rc = []
        for j in range(4):
            rc.append('00')
        maTranKq.append(rc)
    for i in range(4):
        for j in range(4):
            res = 0
            for k in range(4):
                giaTriState = int(state[i][k], 16)
                giaTriMix = maTranMix[j][k]
                res ^= nhanMaTran(giaTriState, giaTriMix)
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

    stateMIX = changeState(stateSHIFT)
    stateMIX = MIXCOLUMN(stateMIX)
    print("Kết quả của MixColumns:")
    for i in range(4):
        for j in range(4):
            print(stateMIX[j][i], end=' ')
        print()
