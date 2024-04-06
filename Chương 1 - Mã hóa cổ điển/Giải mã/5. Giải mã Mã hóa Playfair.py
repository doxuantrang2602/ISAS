def taoMaTranKhoa(K):
    maTran = []
    # Loại bỏ chữ cái trùng và tạo ma trận từ khóa
    K = "".join(sorted(set(K), key=K.index))
    alPha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Bỏ qua chữ 'J'
    for k in K + alPha:
        if k not in maTran:
            maTran.append(k)
    return [maTran[i:i+5] for i in range(0, 25, 5)]

def timViTri(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return (i, row.index(letter))
    return None

def decodePair(a, b, maTran):
    row_a, col_a = timViTri(a, maTran)
    row_b, col_b = timViTri(b, maTran)
    if row_a == row_b:
        return maTran[row_a][(col_a-1)%5] + maTran[row_b][(col_b-1)%5]
    elif col_a == col_b:
        return maTran[(row_a-1)%5][col_a] + maTran[(row_b-1)%5][col_b]
    else:
        return maTran[row_a][col_b] + maTran[row_b][col_a]

def giaiMaPlayfair(C, K):
    maTranKhoa = taoMaTranKhoa(K)
    M = ""
    for i in range(0, len(C), 2):
        M += decodePair(C[i], C[i + 1], maTranKhoa)
    return M

if __name__ == "__main__":
    K = "BEAUTY"
    C = "EAUTBGHVPOHFWH"
    M_giaiMa = giaiMaPlayfair(C, K)
    print("=> Bản rõ sau khi giải mã:", M_giaiMa)
