try:
    n = int(input('Bảng cửu chương cửu: '))
    if n < 1 or n > 9:
        print("n phải nằm trong khoảng từ 1 đến 9")
    else:   
        for i in range(1, 11):
            result = n * i
            print(n, "x", i, "=", result)
except ValueError:
    print("Lỗi! Vui lòng nhập một số nguyên.")