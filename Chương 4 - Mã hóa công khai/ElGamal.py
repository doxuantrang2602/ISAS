def mod(a, xA, q):
    return pow(a, xA, q)

def modNghichDao(a, q):
    for i in range(1, q):
        if (a * i) % q == 1:
            return i
    return None

#Test q = 7001, a = 6, xA = 382, k = 589, M = 442

if __name__ == '__main__':
    q = int(input('Nhập q: '))
    a = int(input('Nhập a: '))
    xA = int(input('Nhập xA: '))
    
    #a. Khóa công khai PU = {q, a, yA} ; yA = a^xA mod q
    yA =  mod(a, xA, q)
    print('Khóa công khai PU = "{{a, q, yA}}" = {{ {}, {}, {} }}'.format(q, a, yA))
    print('-' *50)
    
    #b. Ba chọn k để mã hóa M (k, M nhập từ bàn phím), bản mã là (C1, C2)
    # C1 = a^k mod q, C2 = KM mod q với K = yA^k mod q
    k = int(input('Nhập k: '))
    M = int(input('Nhập M: '))
    C1 = mod(a, k, q)
    K = mod(yA, k, q)
    C2 = (K*M) % q
    print('Bản mã (C1, C2) là: ({}, {})'.format(C1, C2))
    print('-' * 50)
   
   #c. Cách An giải mã (C1, C2) : K = C1^xA mod q, M = (C2K^-1) mod q = (C2 mod q * K^-1 mod q) mod q
    K_giai = mod(C1, xA, q)
    M_giai = ((C2 % q) * modNghichDao(K_giai, q)) % q
    print('An giải bản mã (C1, C2) được K = {}, M = {}'.format(K_giai, M_giai))