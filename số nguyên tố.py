print("kiểm tra n có phải số nguyên tố không")
n = int(input('Nhập số n: '))
if n<2: 
	print('n không phải là số nguyên tố')
else:
	for i in range(2, n//2 +1 ):
		if n % i == 0:
			print('n không phải là số nguyên tố')
		break
	else:
		print ('n là số nguyên tố')


