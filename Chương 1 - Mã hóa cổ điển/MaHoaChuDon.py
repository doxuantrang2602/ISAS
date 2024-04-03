'''
Input: M = EVERYONEHASTHEIR
Key: K = PEINVRXLASWCBYHMOFGKZUQDTJ
Tìm Output: C =
'''
if __name__ == "__main__":
    lstApha= ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    M = list(input("Nhập M = "))
    K = list(input("Nhập K = "))
    Alpha = {}
    for i in range(0,26):
        Alpha[lstApha[i]] = i # Ánh xạ chỉ số cho mỗi chữ cái 'A':0, 'B':1, ..., 'Z':25)
    C = []
    for m in M:
        if m in Alpha:
            i = Alpha[m] # tìm vị trí i của kí tự m trong Alpha
            C.append(K[i]) # Tìm kí tự K[i] để thêm vào Output C
    print("=> Output C = ",''.join(C), sep="")
