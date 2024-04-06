def Solve(C, K):
    lstAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Alpha = {}
    for i in range(0, 26):
        Alpha[lstAlpha[i]] = i
    M = []
    while len(K) < len(M):  # Lặp khi độ dài khóa K < M
        K += M[:len(M) - len(K)]   # Mở rộng K bằng cách thêm vào đầu của M cho đến khi len(K) = len(M)
    print("============================================================")
    print(f'| {"C":<5} | {"K":<5} | {"C index":<8} | {"K index":<8} | {"M index":<8} | {"M"} |')
    print("============================================================")
    for i, c in enumerate(C):
        c_index = Alpha[c]
        if i < len(K):
            k_index = Alpha[K[i]]
        else:
            k_index = Alpha[M[i - len(K)]]
        m_index = (c_index - k_index) % 26
        M.append(lstAlpha[m_index])
        print(f'| {c:<5} | {lstAlpha[k_index]:<5} | {c_index:<8} | {k_index:<8} | {m_index:<8} | {lstAlpha[m_index]} |')
    return ''.join(M)

if __name__ == "__main__":
    C = "HVZRQFMZDRLDPGM"
    K = "WHENIN"

    M_res = Solve(C, K)
    print("============================================================")
    print(f"Bản rõ sau khi giải mã Vigenere AutoKey: {M_res}")
