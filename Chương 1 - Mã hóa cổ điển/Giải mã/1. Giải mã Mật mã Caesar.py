def solveCeasar(C, K):
    lstAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Alpha = {}
    for i in range(0, 26):
        Alpha[lstAlpha[i]] = i
    M_giai = []  # Lưu bản rõ

    for c in C.upper():  # Chuyển bản mã C sang chữ hoa
        if c in Alpha:  # Kiểm tra xem kí tự c có trong bảng chữ cái không
            p = Alpha[c]  # Tìm vị trí của kí tự c trong bảng chữ cái
            m = (p - K) % 26  # Tính vị trí mới sau khi đã dịch chuyển ngược K
            M_giai.append(lstAlpha[m])  # Thêm kí tự giải mã vào bản rõ
        else:
            M_giai.append(c)  # Nếu kí tự không phải chữ cái, giữ nguyên

    return ''.join(M_giai)  # Chuyển list kí tự thành chuỗi

if __name__ == "__main__":
    C = "STSVTWYAFFAFYESC"
    K = 18
    M_res = solveCeasar(C, K)
    print(f"=> Bản rõ sau khi giải mã C với K = {K} là: {M_res}")
