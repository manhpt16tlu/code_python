#đếm số các chữ số của số nguyên dương n
i=0
while True:
   n=int(input('nhap số nguyên dương n: '))
   if n>=0:
   	 break
a=n
while True:
   n=n//10
   i=i+1
   if n==0:
   	break
print('số các chữ số của số ',a,' là: ',i)