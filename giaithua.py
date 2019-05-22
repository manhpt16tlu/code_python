#tinhgiaithua

print('nhap so tu nhien n')
n=int(input())
a=1
s=1
if n==0:
	print('0!=1')
for i in range(n):#i lặp từ 0 đến n-1
	s=s*a
	a=a+1
'''s là giai thừa cần tính 
tăng a lên 1 đơn vị'''
print(n,'!=',s)
	

