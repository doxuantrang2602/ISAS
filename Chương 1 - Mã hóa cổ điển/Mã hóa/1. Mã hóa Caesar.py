'''
Mật mã Ceasar
Input: M = ABADBEGINNINGMAK
Key: K = 18
-> Tìm Output: C = STSVTWYAFFAFYESC
'''

if __name__ == "__main__":
    lstAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    M = "ABADBEGINNINGMAK"
    K = 18
    Alpha = {}
    for i in range(len(lstAlpha)):
        Alpha[lstAlpha[i]] = i
    C = ""
    for m in M:
        if m in Alpha:
            p = Alpha[m]
            c = (p+K) % 26
            for v, k in Alpha.items():
                if k == c:
                    C += v
                    break
    print(f"Output C = {C}")
