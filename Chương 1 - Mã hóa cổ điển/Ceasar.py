'''
Mật mã Ceasar
Input: M = ABADBEGINNINGMAK
Key: K = 18
-> Tìm Output: C =
'''

if __name__ == "__main__":
    lstAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    M = input("Nhập M = ")
    K = int(input("Nhập K = "))
    M = list(M.upper()) # Chuyển đổi chuỗi M nhập vào thành 1 list và chuyển sang dạng chữ hoa
    Alpha = {}
    for i in range(0,26):
        Alpha[lstAlpha[i]] = i # Cấp phát chỉ số cho mỗi chữ cái 'A':0, 'B':1, ..., 'Z':25)
    C = [] #Lưu Output C
    for m in M:
        if m in Alpha: # Kiểm tra xem m có trong bảng chữ cái không
            p = Alpha[m] # Tìm vị trí p của kí tự đó trong Dic Alpha
            c = (p+K)%26 # Tính vị trí mới của kí tự sau khi đã dịch chuyển K
            for v, k in Alpha.items(): # v: key (A->Z), k: value(chỉ số tương ứng)
                if k == c:
                    C.append(v) # Thêm kí tự v vào list C
                    break
    M = ''.join(M) # Chuyển M lại thành chuỗi
    print("=> Kết quả của mật mã Ceasar với M = {}, K = {} là: {}".format(K, M, ''.join(C), sep = ""))

