money=int(input('Nhap so tien: '))
if money > 150:
        tt=money - 50
        print('Duoc giam gia 50$. So tien phai tra la:',tt,'$')
elif 100<= money <150:
        tt=money - 25
        print('Duoc giam gia 25$. So tien phai tra la:',tt,'$')
elif 75<= money <100:
        tt=money - 15
        print('Duoc giam gia 15$. So tien phai tra la:',tt,'$')
else:

        print('Duoc giam gia 0$. So tien phai tra la:',money,'$')