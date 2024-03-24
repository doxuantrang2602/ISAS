lstApha= ['A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
M= list(input("Nhập M: "))
K= list(input("Nhập K: "))
Alpha={}
for i in range(0,26):
    Alpha[lstApha[i]]=i
C = []
for m in M:
    i= Alpha[m]
    C.append(K[i])
print(*C, sep="")
