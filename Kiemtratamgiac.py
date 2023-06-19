print('Nhap cac canh cua tam giac')
a=float(input("nhap canh a: "))
b=float(input("nhapcanh b: "))
c=float(input("nhap canh c: "))
tg=(a + b > c) and (a + c > b) and (b + c > a) and (a!=0) and (b!=0) and (c!=0)
print('kiem tra 3 canh co phai la tam giac: ',tg)

tg_deu = ((a==b==c) and (a!=0) and (b!=0) and (c!=0)) and tg 
print('tam giac deu: ',tg_deu)

tg_can= ((a==b) or (a==c) or (b==c)) and ((a!=0) and (b!=0) and (c!=0)) and tg 
print('tam giac can : ',tg_can)

tg_vuong = tg and ((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b))  and ((a!=0) and (b!=0) and (c!=0))
print('tam giac vuong: ',tg_vuong)

tg_thuong = tg and not tg_deu and not tg_vuong
print('tam giac thuong: ',tg_thuong)