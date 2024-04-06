def solveMaHoaChuDon(M, K):
    lstAlpha= ['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    AlphaInverse = {}
    for i in range(len(K)):
        AlphaInverse[K[i]] = lstAlpha[i] # Ánh xạ từ khóa K trở lại bảng chữ cái lstAlpha
    M_giai = []  # Lưu bản rõ
    for c in M:
        if c in AlphaInverse:
            M_giai.append(AlphaInverse[c]) # Thêm kí tự được ánh xạ từ K trở lại lstAlpha vào bản rõ
    return ''.join(M_giai)  # Chuyển list kí tự thành chuỗi

if __name__ == "__main__":
    C = "VUVFTHYVLPGKLVAF"
    K = "PEINVRXLASWCBYHMOFGKZUQDTJ"
    M_res = solveMaHoaChuDon(C, K)
    print(f"Bản rõ sau khi giải mã: {M_res}")
