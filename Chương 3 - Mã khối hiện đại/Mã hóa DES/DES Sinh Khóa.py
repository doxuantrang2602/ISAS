# Hoán vị PC-1
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

# Hoán vị PC-2
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# Số lần dịch vòng cho mỗi vòng
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def hex_to_bin(hex_str):
    bin_str = bin(int(hex_str, 16))[2:].zfill(64)
    return bin_str


def permute(k, arr, n):
    permutation = ""
    for i in range(n):
        permutation += k[arr[i] - 1]
    return permutation


def left_shift(k, nth_shifts):
    s = SHIFT[nth_shifts]
    return k[s:] + k[:s]


def generate_keys(K):
    K = hex_to_bin(K)
    # Bước 1: Tính C0 và D0
    K_plus = permute(K, PC1, 56)
    C0, D0 = K_plus[:28], K_plus[28:]

    # Bước 2 và 3: Tính Ci, Di và Ki
    keys = []
    Ci, Di = C0, D0
    for i in range(16):
        Ci = left_shift(Ci, i)
        Di = left_shift(Di, i)
        CDi = Ci + Di
        Ki = permute(CDi, PC2, 48)
        keys.append(Ki)
    return keys


if __name__ == "__main__":
    K = "03756CD378146EC7"
    keys = generate_keys(K)
    for i, key in enumerate(keys, start=1):
        print(f"K{i} = {key}")
