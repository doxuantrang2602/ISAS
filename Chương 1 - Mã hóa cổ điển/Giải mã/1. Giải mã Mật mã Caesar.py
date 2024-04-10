if __name__ == "__main__":
    dicAlpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    C = "STSVTWYAFFAFYESC"
    K = 18
    M = ""
    for c in C:
        if c in dicAlpha:
            p = dicAlpha[c]
            m = (p-K)%26
            for k, v in dicAlpha.items():
                if v == m:
                    M += k
                    break
        else:
            M += c
    print(f"Bản rõ M = {M}")

