'''
Mật mã Ceasar
Input: M = ABADBEGINNINGMAK
Key: K = 18
=> Tìm Output: C = STSVTWYAFFAFYESC
'''
if __name__ == "__main__":
    dicAlpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    M = "ABADBEGINNINGMAK"
    K = 18
    C = ""
    for m in M:
        if m in dicAlpha:
            p = dicAlpha[m]
            c = (p+K)%26
            for k,v in dicAlpha.items():
                if v == c:
                    C += k
                    break
        else:
            C += m
    print(f"Output C = {C}")
