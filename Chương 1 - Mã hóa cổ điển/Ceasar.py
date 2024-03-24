lstApha= ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

M= input("Nhập M: ")
K= int(input("Nhập K: "))
M= list(M)
Alpha={}
for i in range(0,26):
    Alpha[lstApha[i]]=i
C=[]
for m in M:
    p= Alpha[m]
    c= (p+K)%26
    for v,k in Alpha.items():
        if k==c:
            C.append(v)
    M= ''.join(M)

print("Kết quả của mật mã Caesar với M={}, K= {} là : {}".format(M,K,''.join(C), sep=""))



