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
def hex_to_matrix(hex_string):
    # Chuyển đổi chuỗi hex thành ma trận 4x4
    matrix = [['00' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[j][i] = hex_string[i*8 + j*2 : i*8 + j*2 + 2]
    return matrix

def XOR_bytes(byte1, byte2):
    # Thực hiện phép XOR giữa 2 byte
    return hex(int(byte1, 16) ^ int(byte2, 16))[2:].zfill(2).upper()

def AddRoundKey(M, K):
    # Chuyển đổi M và K thành ma trận 4x4
    M_matrix = hex_to_matrix(M)
    K_matrix = hex_to_matrix(K)
    # Thực hiện phép XOR giữa từng byte của M và K
    state = [['00' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[i][j] = XOR_bytes(M_matrix[i][j], K_matrix[i][j])

    return state

def SubByte(state):
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            state[i][j] = Sbox[byte.upper()]
    return state

def ShiftRows(state):
    # Dịch vòng trái hàng thứ hai một byte
    state[1] = state[1][1:] + state[1][:1]
    # Dịch vòng trái hàng thứ ba hai byte
    state[2] = state[2][2:] + state[2][:2]
    # Dịch vòng trái hàng thứ tư ba byte
    state[3] = state[3][3:] + state[3][:3]
    return state


def MixColumns(state):
    # Ma trận thực hiện phép nhân
    mul_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    # Tạo một ma trận tạm thời để lưu trữ kết quả
    result_matrix = [['00' for _ in range(4)] for _ in range(4)]

    # Thực hiện phép nhân với ma trận
    for i in range(4):
        for j in range(4):
            result = 0
            for k in range(4):
                result ^= GF_multiply(mul_matrix[i][k], int(state[k][j], 16))
            result_matrix[i][j] = format(result, '02x').upper()

    return result_matrix


def GF_multiply(a, b):
    # Thực hiện phép nhân trong trường Galois
    result = 0
    while b:
        if b & 1:
            result ^= a
        if a & 0x80:
            a = (a << 1) ^ 0x11B  # 0x11B là xtime(0x80)
        else:
            a <<= 1
        b >>= 1
    return result


if __name__ == "__main__":
    M = "39400A33DB86771F578E208998CDB8A4"
    K = "A2E7F3E9F4EC8BB93217B94C5FD982CD"
    initial_state  = AddRoundKey(M, K)
    print("Kết quả của AddRoundKey:")
    for row in initial_state :
        print(*row)

    state_after_subbyte = SubByte(initial_state)
    print("Kết quả của SubByte:")
    for row in state_after_subbyte:
        print(' '.join(row))

    state_after_shiftrows = ShiftRows(state_after_subbyte)
    print("Kết quả của ShiftRows:")
    for row in state_after_shiftrows:
        print(' '.join(row))

    state_after_mixcolumns = MixColumns(state_after_shiftrows)
    print("Kết quả của MixColumns:")
    for row in state_after_mixcolumns:
        print(' '.join(row))



