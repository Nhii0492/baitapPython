print('BMI')
chieu_cao=float(input('Nhap chieu cao: '))
can_nang=float(input('Nhap can nang: '))
if chieu_cao <=0 or can_nang <=0:
    print('chieu cao va can nang phai lon hon 0')
else:
    BMI= can_nang/(chieu_cao**2)
    if BMI <16:
        print('Gầy cấp độ III')
    elif 16<= BMI <17:
        print('Gầy cấp độ II')
    elif 17<= BMI <18.5:
        print('Gầy cấp độ I')
    elif 18.5<= BMI <25:
        print('Bình thường')
    elif 25<= BMI <30:
        print('Thừa cân')
    elif 30<= BMI <35:
        print('Béo phì cấp độ I')
    elif 35<= BMI <40:
        print('Béo phì cấp độ II')
    elif BMI >40:
            print('Béo phì cấp độ III')