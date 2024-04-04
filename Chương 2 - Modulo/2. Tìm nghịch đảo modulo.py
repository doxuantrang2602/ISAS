def euclidMoRong(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = euclidMoRong(b % a, a)
        return (g, y - (b // a) * x, x)

def tinhModNghichDao(a, n):
    g, x, y = euclidMoRong(a, n)
    if g != 1:
        raise Exception('Nghịch đảo không tồn tại')
    else:
        return x % n

if __name__ == "__main__":
    a = int(input("Nhập a = "))
    n = int(input("Nhập n = "))
    x = tinhModNghichDao(a, n) # Tính x = a^(-1) mod n
    print(f"=> Output x = {x}")