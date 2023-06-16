print('Tinh chu vi va dien tich hinh tron')
r = float(input("Nhập bán kính đường tròn: "))
if r<=0:
	print("ban kinh r phai >0")
else:
	p=r*2*3.14
	s=r**2*3.14
	print("Chu vi hình tròn: ",p)
	print("Dien tích hình tròn: ",s)