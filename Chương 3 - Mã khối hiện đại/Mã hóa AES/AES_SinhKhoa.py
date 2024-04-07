'''
Sinh khóa
Viết hàm KeyExpansion mở rộng khóa từ khóa K (16 byte) thành 176 byte (11 x 16 byte)
Input: K mảng 16 byte
Output: K+ mảng 176 byte

PHẦN 1: SINH 10 KHÓA Ki từ khóa K (input), i = 1, 2, ..., 10. (Mục 5.4)
1. Chia khóa K (128 bit) thành 4 word (32 bit)
Input: K (input) = A2E7F3E9F4EC8BB93217B94C5FD982CD,
Output: w0 = , w1 = , w2 = , w3 = ,
2. Dịch vòng trái 1 byte đối với w3 (32 bit)
Input: w3 (kết quả bài 1) =
Output: rw = RotWord(w3) =
3. Thay thế từng byte trong rw bằng bảng S-box SubWord
Input: rw (kết quả bài 2) = ; Sbox (tài liệu mục 5.3, Table 5.2, trang 157)
Output: sw = SubWord(rw) =
4. sw XORbit với Rcon[j]
Input: sw (kết quả bài 3) = ; RC[i] (xem tài liệu mục 5.4 Key Expansion)
Output: xcsw = XorRcon(sw, RC[i]) =
5. Tính khóa K1 = (w4, w5, w6, w7)
Input: xcsw (kết quả bài 4) = ; w0, w1, w2, w3 (kết quả bài 1);
Output: w4 = XORbit(xcsw, w0) =
w5 = XORbit(w4, w1) =
w6 = XORbit(w5, w2) =
w7 = XORbit(w6, w3) =
LẶP LẠI từ Bài 2 đến Bài 5 để tạo các khóa K2, K3, ..., K1
'''
'''
M = 39400A33DB86771F578E208998CDB8A4
K = A2E7F3E9F4EC8BB93217B94C5FD982CD
'''
Rcon_expanded = [
    '01000000', '02000000', '04000000', '08000000',
    '10000000', '20000000', '40000000', '80000000',
    '1B000000', '36000000'
]
s_box = {
    '00': '63', '01': '7C', '02': '77', '03': '7B', '04': 'F2', '05': '6B', '06': '6F', '07': 'C5', '08': '30',
    '09': '01', '0A': '67', '0B': '2B', '0C': 'FE', '0D': 'D7', '0E': 'AB', '0F': '76',
    '10': 'CA', '11': '82', '12': 'C9', '13': '7D', '14': 'FA', '15': '59', '16': '47', '17': 'F0', '18': 'AD',
    '19': 'D4', '1A': 'A2', '1B': 'AF', '1C': '9C', '1D': 'A4', '1E': '72', '1F': 'C0',
    '20': 'B7', '21': 'FD', '22': '93', '23': '26', '24': '36', '25': '3F', '26': 'F7', '27': 'CC', '28': '34',
    '29': 'A5', '2A': 'E5', '2B': 'F1', '2C': '71', '2D': 'D8', '2E': '31', '2F': '15',
    '30': '04', '31': 'C7', '32': '23', '33': 'C3', '34': '18', '35': '96', '36': '05', '37': '9A', '38': '07',
    '39': '12', '3A': '80', '3B': 'E2', '3C': 'EB', '3D': '27', '3E': 'B2', '3F': '75',
    '40': '09', '41': '83', '42': '2C', '43': '1A', '44': '1B', '45': '6E', '46': '5A', '47': 'A0', '48': '52',
    '49': '3B', '4A': 'D6', '4B': 'B3', '4C': '29', '4D': 'E3', '4E': '2F', '4F': '84',
    '50': '53', '51': 'D1', '52': '00', '53': 'ED', '54': '20', '55': 'FC', '56': 'B1', '57': '5B', '58': '6A',
    '59': 'CB', '5A': 'BE', '5B': '39', '5C': '4A', '5D': '4C', '5E': '58', '5F': 'CF',
    '60': 'D0', '61': 'EF', '62': 'AA', '63': 'FB', '64': '43', '65': '4D', '66': '33', '67': '85', '68': '45',
    '69': 'F9', '6A': '02', '6B': '7F', '6C': '50', '6D': '3C', '6E': '9F', '6F': 'A8',
    '70': '51', '71': 'A3', '72': '40', '73': '8F', '74': '92', '75': '9D', '76': '38', '77': 'F5', '78': 'BC',
    '79': 'B6', '7A': 'DA', '7B': '21', '7C': '10', '7D': 'FF', '7E': 'F3', '7F': 'D2',
    '80': 'CD', '81': '0C', '82': '13', '83': 'EC', '84': '5F', '85': '97', '86': '44', '87': '17', '88': 'C4',
    '89': 'A7', '8A': '7E', '8B': '3D', '8C': '64', '8D': '5D', '8E': '19', '8F': '73',
    '90': '60', '91': '81', '92': '4F', '93': 'DC', '94': '22', '95': '2A', '96': '90', '97': '88', '98': '46',
    '99': 'EE', '9A': 'B8', '9B': '14', '9C': 'DE', '9D': '5E', '9E': '0B', '9F': 'DB',
    'A0': 'E0', 'A1': '32', 'A2': '3A', 'A3': '0A', 'A4': '49', 'A5': '06', 'A6': '24', 'A7': '5C', 'A8': 'C2',
    'A9': 'D3', 'AA': 'AC', 'AB': '62', 'AC': '91', 'AD': '95', 'AE': 'E4', 'AF': '79',
    'B0': 'E7', 'B1': 'C8', 'B2': '37', 'B3': '6D', 'B4': '8D', 'B5': 'D5', 'B6': '4E', 'B7': 'A9', 'B8': '6C',
    'B9': '56', 'BA': 'F4', 'BB': 'EA', 'BC': '65', 'BD': '7A', 'BE': 'AE', 'BF': '08',
    'C0': 'BA', 'C1': '78', 'C2': '25', 'C3': '2E', 'C4': '1C', 'C5': 'A6', 'C6': 'B4', 'C7': 'C6', 'C8': 'E8',
    'C9': 'DD', 'CA': '74', 'CB': '1F', 'CC': '4B', 'CD': 'BD', 'CE': '8B', 'CF': '8A',
    'D0': '70', 'D1': '3E', 'D2': 'B5', 'D3': '66', 'D4': '48', 'D5': '03', 'D6': 'F6', 'D7': '0E', 'D8': '61',
    'D9': '35', 'DA': '57', 'DB': 'B9', 'DC': '86', 'DD': 'C1', 'DE': '1D', 'DF': '9E',
    'E0': 'E1', 'E1': 'F8', 'E2': '98', 'E3': '11', 'E4': '69', 'E5': 'D9', 'E6': '8E', 'E7': '94', 'E8': '9B',
    'E9': '1E', 'EA': '87', 'EB': 'E9', 'EC': 'CE', 'ED': '55', 'EE': '28', 'EF': 'DF',
    'F0': '8C', 'F1': 'A1', 'F2': '89', 'F3': '0D', 'F4': 'BF', 'F5': 'E6', 'F6': '42', 'F7': '68', 'F8': '41',
    'F9': '99', 'FA': '2D', 'FB': '0F', 'FC': 'B0', 'FD': '54', 'FE': 'BB', 'FF': '16'
}
def split_key(K):
    w0 = K[:8]
    w1 = K[8:16]
    w2 = K[16:24]
    w3 = K[24:]
    return w0, w1, w2, w3

def RotWord(word):
    return word[2:] + word[:2]

def SubWord(word):
    sw = ""
    for i in range(0, len(word), 2):
        sw += s_box[word[i:i+2]]
    return sw

def XORbit(word1, word2):
    result = ""
    for i in range(0, len(word1), 2):
        # Chuyển từng cặp ký tự hex thành số, thực hiện XOR và chuyển kết quả trở lại dạng hex
        xor_result = hex(int(word1[i:i+2], 16) ^ int(word2[i:i+2], 16))[2:].zfill(2)
        result += xor_result
    return result.upper()

def KeyExpansion(K):
    keys = [K]  # Lưu khóa ban đầu
    w = split_key(K)  # Chia khóa K thành 4 từ w0, w1, w2, w3

    # Lặp qua 10 vòng để sinh ra 10 khóa con
    for i in range(10):
        # Áp dụng các bước sinh khóa
        rw = RotWord(w[3])
        sw = SubWord(rw)
        xcsw = XORbit(sw, Rcon_expanded[i])
        w4 = XORbit(xcsw, w[0])
        w5 = XORbit(w4, w[1])
        w6 = XORbit(w5, w[2])
        w7 = XORbit(w6, w[3])

        # Cập nhật các từ cho vòng lặp tiếp theo
        w = (w4, w5, w6, w7)

        # Nối các từ lại để tạo thành khóa mới và thêm vào danh sách khóa
        new_key = w4 + w5 + w6 + w7
        keys.append(new_key)

    return keys

if __name__ == "__main__":
    K = "A2E7F3E9F4EC8BB93217B94C5FD982CD"
    expanded_keys = KeyExpansion(K)
    for i, key in enumerate(expanded_keys):
        print(f"Khóa K{i}: {key}")