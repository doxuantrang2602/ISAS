'''
Input: M = LOVEISBLINDLOVE
Key: K = WHENIN
Tìm Output: C =
'''
if __name__ == '__main__':
    lstAlpha= ['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    M= list(input("Nhập M = "))
    K= list(input("Nhập K = "))
    Alpha = {}
    for i in range(0,26):
        Alpha[lstAlpha[i]] = i # Ánh xạ chỉ số i cho mỗi kí tự
    # Xử lý mở rộng K
    moRong_K = K * (len(M) // len(K)) + K[:len(M) % len(K)]

    C = []  # Output C kết quả

    print(f'{"M":<5} | {"K":<5} | {"M index":<8} | {"K index":<8} | {"C index":<8} | {"C"}') # In tiêu đề cho bảng

    for m, k in zip(M, moRong_K):
        m_index = Alpha[m]  # Chỉ số của ký tự m trong bảng chữ cái
        k_index = Alpha[k]  # Chỉ số của ký tự k trong bảng chữ cái
        c_index = (m_index + k_index) % 26  # Chỉ số mới cho ký tự mã hóa
        C.append(lstAlpha[c_index])
        print(f'{m:<5} | {k:<5} | {m_index:<8} | {k_index:<8} | {c_index:<8} | {lstAlpha[c_index]}')
    print("Kết quả của Vigenere lặp khóa: ",''.join(C), sep="")

