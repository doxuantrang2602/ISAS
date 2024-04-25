'''
1. TÍNH LŨY THỪA MODULO 𝒃 = 𝒂^𝒎 𝒎𝒐𝒅 𝒏 BẰNG CÁCH HẠ BẬC LŨY THỪA
Input: a = 449; m = 6763; n = 6763
Tìm Output: b = 449
'''

def tinhLuyThuaModulo(a,m,n):
    D = {}
    i = 1
    while i <= m:
        D[i] = pow(a, i, n)
        i *= 2
    print(f"|  {'i':<6} |  {'a^i mod n':<10} |")
    print(f"--------------------------")
    for p, v in D.items():
        print(f"|  {p:<6} |  {v:<10} |")
    res = 1
    for p in sorted(D.keys(), reverse=True):
        if m >= p:
            res = (res * D[p]) % n
            m -= p
    return res

if __name__ == "__main__":
    a = 449
    m = 6763
    n = 6763
    res = tinhLuyThuaModulo(a,m,n)
    print(f"=> a^m mod n = {res}")
