def taoMaTranKhoa(K):
    maTran = []
    K = "".join(sorted(set(K), key=K.index))
    alPha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    dsDuyNhat = []
    for k in K + alPha:
        if k not in dsDuyNhat:
            dsDuyNhat.append(k)
    for i in range(0, 25, 5):
        maTran.append(dsDuyNhat[i:i + 5])
    return maTran

def timViTri(x, maTran):
    for i, row in enumerate(maTran):
        if x in row:
            return (i, row.index(x))
    return None

def giaiMaPlayfair(a, b, maTran):
    hang_a, cot_a = timViTri(a, maTran)
    hang_b, cot_b = timViTri(b, maTran)
    if hang_a == hang_b:
        return maTran[hang_a][(cot_a-1)%5] + maTran[hang_b][(cot_b-1)%5]
    elif cot_a == cot_b:
        return maTran[(hang_a-1)%5][cot_a] + maTran[(hang_b-1)%5][cot_b]
    else:
        return maTran[hang_a][cot_b] + maTran[hang_b][cot_a]

if __name__ == "__main__":
    K = "BEAUTY"
    C = "EAUTBGHVPOHFWH"
    maTranKhoa = taoMaTranKhoa(K)
    M = ""
    for i in range(0, len(C), 2):
        M += giaiMaPlayfair(C[i], C[i + 1], maTranKhoa)
    print("=> Bản rõ sau khi giải mã:", M)
