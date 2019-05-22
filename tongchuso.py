#tinh tổng các chữ số của số tự nhiên dương 
print("hello,i'im python")
sum=0
while True:
    n=int(input('nhap so tự nhiên dương: '))
    if n>0:
    	break
a=n   	
while True:
	sum=sum+(n%10)#hàm % chia lấy phần dư
	n=n//10#chia lấy phần nguyên
	if n==0:
		pass
		break
print('tong cac chu so cua',a,' la : ',sum)

	