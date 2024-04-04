def gf_mul(x, y):
    r = 0
    for i in range(8):
        if y & 1 == 1:
            r ^= x
        hbit = x & 0x80
        x <<= 1
        if hbit == 0x80:
            x ^= 0x1b
        y >>= 1
    return r % 256

def mix_columns(s):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for c in range(4):
        result[0][c] = gf_mul(0x02, s[0][c]) ^ gf_mul(0x03, s[1][c]) ^ s[2][c] ^ s[3][c]
        result[1][c] = s[0][c] ^ gf_mul(0x02, s[1][c]) ^ gf_mul(0x03, s[2][c]) ^ s[3][c]
        result[2][c] = s[0][c] ^ s[1][c] ^ gf_mul(0x02, s[2][c]) ^ gf_mul(0x03, s[3][c])
        result[3][c] = gf_mul(0x03, s[0][c]) ^ s[1][c] ^ s[2][c] ^ gf_mul(0x02, s[3][c])
    return result

# Your matrix
matrix = [
    [0x79, 0x4E, 0xAA, 0x02],
    [0x6F, 0x12, 0xA6, 0x18],
    [0x19, 0x28, 0x73, 0x86],
    [0xBF, 0xC0, 0xD0, 0x15]
]

mixed_matrix = mix_columns(matrix)

for row in mixed_matrix:
    print(' '.join([format(cell, '02X') for cell in row]))
