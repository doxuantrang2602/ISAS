'''
MẬT MÃ MA TRẬN KHÓA PLAYFAIR
Input: M = BEAUTYISONLYSK
Key: K = BEAUTY
Tìm Output: C = EAUTBGHVPOHFWH
'''

def taoMaTranKhoa(K):
    maTran = []
    K = "".join(sorted(set(K), key = K.index))
    alPha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    dsDuyNhat = []
    for k in K + alPha:
        if k not in dsDuyNhat:
            dsDuyNhat.append(k)
    for i in range(0, 25, 5):
        maTran.append(dsDuyNhat[i:i+5])
    return maTran

def tempM(M):
    tmpText = ""
    i = 0
    while i < len(M):
        tmpText += M[i]
        if i+1 < len(M) and M[i] == M[i+1]:
            tmpText += "X"
        if i+1 < len(M):
            tmpText += M[i+1]
        i+=2
    if len(tmpText) %2 != 0:
        tmpText += "X"
    return tmpText

def timViTri(x, maTran):
    for i, row in enumerate(maTran):
        if x in row:
            return (i, row.index(x))
    return None

def encodePair(a, b, maTran):
    hang_a, cot_a = timViTri(a, maTran)
    hang_b, cot_b = timViTri(b, maTran)
    if hang_a == hang_b:
        return maTran[hang_a][(cot_a+1)%5] + maTran[hang_b][(cot_b+1)%5]
    elif cot_a == cot_b:
        return maTran[(hang_a+1)%5][cot_a] + maTran[(hang_b+1)%5][cot_b]
    else:
        return maTran[hang_a][cot_b] + maTran[hang_b][cot_a]

if __name__ == "__main__":
    M = "BEAUTYISONLYSK"
    K = "BEAUTY"
    maTranKhoa = taoMaTranKhoa(K)
    for row in maTranKhoa:
        print(' '.join(row))
    M = tempM(M)
    print(M)
    C = ""
    for i in range(0, len(M), 2):
        C += encodePair(M[i], M[i+1], maTranKhoa)
    print("=> Output C = ", C)
