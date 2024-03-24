import math
def Tinh_Mod(a,i, n):
    return pow(a,i, n)
def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:  #
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

if __name__ == '__main__':
    a=int(input("Nhập a:"))
    b=int(input("Nhập b:"))
    n=int(input("Nhập n: "))

    for i in range(1,euler_phi(n)):
        p= Tinh_Mod(a,i,n)
        if p==b:
            print("log{} {} (mod {}) = {}".format( a,b,n,i))
            break
    else:
        print("Khong ton tai ")
