try:
    string = input('Nhập 2 số bất kỳ cách nhau bằng dấu phẩy (,): ')
    so = string.split(",")
    start = int(so[0].strip())
    end = int(so[1].strip())
    print("start =", start)
    print("end =", end)
    if end < start:
        start, end = end, start
    for num in range(start, end + 1):   
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
except ValueError:
    print("Lỗi! Vui lòng nhập 2 số nguyên cách nhau bằng dấu phẩy (,).")
except IndexError:
    print("Lỗi! Vui lòng nhập đúng định dạng 2 số cách nhau bằng dấu phẩy (,).")
except:
    print("Lỗi không xác định!")