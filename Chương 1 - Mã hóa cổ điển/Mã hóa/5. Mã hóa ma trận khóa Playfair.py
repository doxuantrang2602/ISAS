'''
MẬT MÃ MA TRẬN KHÓA PLAYFAIR
Input: M = BEAUTYISONLYSK
Key: K = BEAUTY
Tìm Output: C = EAUTBGHVPOHFWH
'''

def taoMaTranKhoa(K):
    maTran = []
    # Loại bỏ chữ cái trùng và tạo ma trận từ khóa
    K = "".join(sorted(set(K), key=K.index))
    alPha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Bỏ qua chữ 'J'
    for k in K + alPha:
        if k not in maTran:
            maTran.append(k)
    return [maTran[i:i+5] for i in range(0, 25, 5)]

def tempM(M):
    preparedText = ""
    i = 0
    while i < len(M):
        preparedText += M[i]
        if i+1 < len(M) and M[i] == M[i+1]:
            preparedText += 'X'
        if i+1 < len(M):
            preparedText += M[i+1]
        i += 2
    if len(preparedText) % 2 != 0:
        preparedText += 'X'
    return preparedText

def timViTri(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return (i, row.index(letter))
    return None

def encodePair(a, b, maTran):
    row_a, col_a = timViTri(a, maTran)
    row_b, col_b = timViTri(b, maTran)
    if row_a == row_b:
        return maTran[row_a][(col_a+1)%5] + maTran[row_b][(col_b+1)%5]
    elif col_a == col_b:
        return maTran[(row_a+1)%5][col_a] + maTran[(row_b+1)%5][col_b]
    else:
        return maTran[row_a][col_b] + maTran[row_b][col_a]

if __name__ == "__main__":
    M = "BEAUTYISONLYSK"
    K = "BEAUTY"
    maTranKhoa = taoMaTranKhoa(K)
    M = tempM(M)
    C = ""
    for i in range(0, len(M), 2):
        C += encodePair(M[i], M[i + 1], maTranKhoa)
    print("=> Output C = ", C)

