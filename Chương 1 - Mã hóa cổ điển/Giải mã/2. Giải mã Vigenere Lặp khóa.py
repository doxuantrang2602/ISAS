def giaiMaVigenere(C, K):
    lstAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Alpha = {char: idx for idx, char in enumerate(lstAlpha)}

    # Xử lý mở rộng K để phù hợp với độ dài của C
    moRong_K = K * (len(C) // len(K)) + K[:len(C) % len(K)]

    M_giai = []  # Lưu bản rõ

    print("======================================================")
    print(f'| {"C":<5} | {"K":<5} | {"C index":<8} | {"K index":<8} | {"M index":<8} | {"M"} |')  # In tiêu đề cho bảng
    print("======================================================")

    for c, k in zip(C, moRong_K):
        c_index = Alpha[c]  # Chỉ số của kí tự c trong bảng chữ cái
        k_index = Alpha[k]  # Chỉ số của kí tự k trong bảng chữ cái
        m_index = (c_index - k_index) % 26  # Tính chỉ số mới cho kí tự giải mã
        M_giai.append(lstAlpha[m_index])  # Thêm kí tự giải mã vào bản rõ
        print(f'| {c:<5} | {k:<5} | {c_index:<8} | {k_index:<8} | {m_index:<8} | {lstAlpha[m_index]} |')
    print("======================================================")
    print("Bản rõ sau khi giải mã Vigenere lặp khóa là: ", ''.join(M_giai), sep="")

if __name__ == "__main__":
    C = "HVZRQFXSMALYKCI"
    K = "WHENIN"
    giaiMaVigenere(C, K)
