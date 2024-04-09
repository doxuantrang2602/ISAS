'''
Mã hóa AES – xây dựng hàm mã hóa AES(x, k) thực hiện mã hóa theo thuật toán AES – 128 bit khóa
input: x, k – chuỗi số 128 bit
Output: y – chuỗi số 128 bít được mã hóa từ x theo thuật toán AES với khóa
'''

from AES_MaHoa import *
from AES_SinhKhoa import *

def maTrixToHex(maTran):
    hexStr = ""
    for i in range(4):
        for j in range(4):
            hexStr += maTran[j][i]
    return hexStr

def AES(x, k):
    keys = keyExpansion(k)
    state = hexToMatrix(x)
    # Vòng 0
    state = ADDROUNDKEY(maTrixToHex(state), keys[0])
    # Vòng 1->9
    for i in range(1,10):
        state = SUBBYTE(state)
        state = SHIFTROW(state)
        state = changeState(state)
        state = MIXCOLUMN(state)
        state = changeState(state)
        state = ADDROUNDKEY(maTrixToHex(state), keys[i])
    # Vòng cuối cùng
    state = SUBBYTE(state)
    state = SHIFTROW(state)
    state = ADDROUNDKEY(maTrixToHex(state), keys[10])
    resHex = maTrixToHex(state)
    return resHex

if __name__ == "__main__":
    M = "0123456789ABCDEFFEDCBA9876543210"
    K = "0F1571C947D9E8590CB7ADD6AF7F6798"
    resAES = AES(M, K)
    print(f"Kết quả mã hóa AES : {resAES}")

'''
M = 39400A33DB86771F578E208998CDB8A4
K = A2E7F3E9F4EC8BB93217B94C5FD982CD
Output: 8D1652411C2A99D058629433F72F601C

M = "0123456789ABCDEFFEDCBA9876543210"
K = "0F1571C947D9E8590CB7ADD6AF7F6798"
Output: ff0b844a0853bf7c6934ab4364148fb9
'''