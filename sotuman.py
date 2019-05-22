import math#gọi đến thư viện math
i=0
s=0
while True:
   n=int(input('nhap số nguyên dương n: '))
   if n>=0:
   	 break
a=n
b=n
while True:
   n=n//10
   i=i+1
   if n==0:
   	break
while True:
   s=s+math.pow((a%10),i)#hàm lũy thừa,có thể dùng toán tử ** 
   a=a//10
   if a==0:
   	break
if s==b:
	print("True")
else:
	print('False')
