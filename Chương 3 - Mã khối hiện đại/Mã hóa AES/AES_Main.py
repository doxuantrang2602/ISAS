'''
Mã hóa AES – xây dựng hàm mã hóa AES(x, k) thực hiện mã hóa theo thuật toán AES – 128 bit khóa
input: x, k – chuỗi số 128 bit
Output: y – chuỗi số 128 bít được mã hóa từ x theo thuật toán AES với khóa
'''

from AES_MaHoa import hex_to_matrix, AddRoundKey, SubByte, ShiftRows, MixColumns
from AES_SinhKhoa import *
def matrix_to_hex(matrix):
    hex_string = ""
    for i in range(4):
        for j in range(4):
            hex_string += matrix[j][i]
    return hex_string

def AES(x, k):
    # Sinh ra tất cả các khóa mở rộng
    expanded_keys = keyExpansion(k)

    # Biến đổi input hex string x thành ma trận state
    state = hex_to_matrix(x)

    # Vòng 0: AddRoundKey trước khi bắt đầu các vòng lặp chính
    state = AddRoundKey(matrix_to_hex(state), expanded_keys[0])

    # 9 vòng đầu tiên bao gồm SubBytes, ShiftRows, MixColumns, và AddRoundKey
    for i in range(1, 10):
        state = SubByte(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(matrix_to_hex(state), expanded_keys[i])

    # Vòng cuối cùng không có MixColumns
    state = SubByte(state)
    state = ShiftRows(state)
    state = AddRoundKey(matrix_to_hex(state), expanded_keys[10])

    # Chuyển đổi state về dạng chuỗi hex để trả về
    encrypted_text = matrix_to_hex(state)
    return encrypted_text


if __name__ == "__main__":
    M = "0123456789ABCDEFFEDCBA9876543210"
    K = "0F1571C947D9E8590CB7ADD6AF7F6798"
    resAES = AES(M, K)
    print(f"Kết quả mã hóa AES : {resAES}")

'''
M = 39400A33DB86771F578E208998CDB8A4
K = A2E7F3E9F4EC8BB93217B94C5FD982CD

M = "0123456789ABCDEFFEDCBA9876543210"
K = "0F1571C947D9E8590CB7ADD6AF7F6798"
'''