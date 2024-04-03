'''
Input: M = LOVEISBLINDLOVE
Key: K = WHENIN
=> Tìm Output: C =
'''
if __name__ == "__main__":
    lstAlpha=['A','B','C','D','E','F','G','H','I','J','K','L','M',
                  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    M= list(input("Nhập M = "))
    K= list(input("Nhập K = "))
    Alpha={}
    for i in range(0,26):
        Alpha[lstAlpha[i]]=i

    while len(K) < len(M): # Lặp khi độ dài khóa K < M
        K += M[:len(M) - len(K)] # Mở rộng K bằng cách thêm vào đầu của M cho đến khi len(K) = len(M)

    C = []
    print("======================================================")
    print(f'| {"M":<5} | {"K":<5} | {"M index":<8} | {"K index":<8} | {"C index":<8} | {"C"} |')  # In tiêu đề cho bảng
    print("======================================================")
    for m, k in zip(M, K):
        c = (Alpha[m] + Alpha[k]) % 26
        for a, b in Alpha.items():
            if b == c:
                C.append(a)
        print(f'| {m:<5} | {k:<5} | {Alpha[m]:<8} | {Alpha[k]:<8} | {c:<8} | {lstAlpha[c]} |')
    print("+> Kết của của Vigenere AutoKey: ",''.join(C), sep="")

