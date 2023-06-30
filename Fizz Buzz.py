try:
    string=input('Nhập 2 số bất kì cách nhau bằng dầu ",": ')
    so=string.split(",")
    start=int(so[0].strip())
    end=int(so[1].strip())
    print("start =",start)
    print("end=",end)
    if end < start:
        tmp = start
        start=end
        end=tmp
    print(start,end)
    for num in range(start, end + 1):   
            if num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            elif num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            else:
                print(num)
except:
    print("error")