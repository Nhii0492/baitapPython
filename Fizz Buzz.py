string=input('Nhập 2 số bất kì cách nhau bằng dầu ",": ')
so=string.split(",")
start=int(so[0])
end=int(so[1])
print("start =",start)
print("end=",end)
for num in range(start, end + 1):   
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)