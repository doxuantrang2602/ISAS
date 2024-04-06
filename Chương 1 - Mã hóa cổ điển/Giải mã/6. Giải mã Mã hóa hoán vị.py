if __name__ == "__main__":
    C = "NAOIPNANIONPNAOIGN"
    K = 9
    M = ""
    soHang = len(C) // K
    for i in range(soHang):
        for j in range(K):
            M += C[j * soHang + i]
    print("=> Bản rõ M =", M)

