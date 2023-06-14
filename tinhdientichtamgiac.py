import math
print("Tính chu vi, diện tích tam giác")
a=float(input("Nhap canh a: "))
b=float(input("Nhap canh b: "))
c=float(input("Nhap canh c: "))
if a<=0 and b<=0 and c<=0:
	print("Nhap lai ")
else:
	p=(a+b+c)/2
		print("chu vi cua tam giac la: ",p)
	s= math.sqrt(p*(p-a)*(p-b)*(p-c))
		print("dien tich cua tam giac la: ",s)

