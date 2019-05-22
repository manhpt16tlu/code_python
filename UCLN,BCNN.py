#tìm ucln và bcnn của a và b
while True:
   a=int(input('nhập số nguyên dương a:'))
   if a>0:
   	break
while True:
   b=int(input('nhập số nguyên dương b:'))
   if b>0:
   	break
m=a
n=b
while a!=b:
	if a>b:
		a=a-b
	else:
		b=b-a
print('ucln của hai số là:',a)
bcnn=int((m*n)/a)
print('bcnn của hai số là: ',bcnn)
