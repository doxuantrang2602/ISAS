'''
Input: M = LOVEISBLINDLOVE
Key: K = WHENIN
Tìm Output: C = HVZRQFXSMALYKCI
'''
if __name__ == '__main__':
    dicAlpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    M = "LOVEISBLINDLOVE"
    K = "WHENIN"
    while len(K) < len(M):
        K += K
    K = K[:len(M)]
    C = ""
    for m, k in zip(M, K):
        if m in dicAlpha and k in dicAlpha:
            m_index = dicAlpha[m]
            k_index = dicAlpha[k]
            c_index = (m_index + k_index) % 26
            for k, v in dicAlpha.items():
                if v == c_index:
                    C += k
                    break
        else:
            C += m
    print(f"Output C = {C}")
