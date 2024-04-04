'''
MẬT MÃ MA TRẬN KHÓA PLAYFAIR
Input: M = BEAUTYISONLYSK
Key: K = BEAUTY
Tìm Output: C =
'''

def create_key_matrix(key):
    matrix = []
    # Loại bỏ chữ cái trùng và tạo ma trận từ khóa
    key = "".join(sorted(set(key), key=key.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Bỏ qua chữ 'J'
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def prepare_text(text):
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            prepared_text += 'X'
        if i+1 < len(text):
            prepared_text += text[i+1]
        i += 2
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'
    return prepared_text

def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return (i, row.index(letter))
    return None

def encode_pair(a, b, matrix):
    row_a, col_a = find_position(a, matrix)
    row_b, col_b = find_position(b, matrix)
    if row_a == row_b:
        return matrix[row_a][(col_a+1)%5] + matrix[row_b][(col_b+1)%5]
    elif col_a == col_b:
        return matrix[(row_a+1)%5][col_a] + matrix[(row_b+1)%5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def encode(text, key):
    matrix = create_key_matrix(key)
    text = prepare_text(text)
    encoded_text = ""
    for i in range(0, len(text), 2):
        encoded_text += encode_pair(text[i], text[i+1], matrix)
    return encoded_text

# Mã hóa
key = "BEAUTY"
text = "BEAUTYISONLYSK"
encoded_text = encode(text, key)
print("Encoded text:", encoded_text)

