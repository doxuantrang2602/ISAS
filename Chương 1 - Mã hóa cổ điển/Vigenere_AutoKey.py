lstApha=['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
M= list(input("Nhập M: "))
K= list(input("Nhập K: "))
Alpha={}
for i in range(0,26):
    Alpha[lstApha[i]]=i

while len(K) < len(M):
    K += M[:len(M) - len(K)]

C = []
for m, k in zip(M, K):
    c = (Alpha[m] + Alpha[k]) % 26
    for a, b in Alpha.items():
        if b == c:
            C.append(a)

print("Kết của của AutoKey: ", *C, sep="")

