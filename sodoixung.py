#kiểm tra số đối xứng
n=int(input('nhap so n: '))
s=str(n)#chuyển n thành chuỗi s
b=s[::-1]#đảo ngược chuỗi s và gán chô biến b
a=int(b)#chuyển chuỗi b thành số và gán cho a
if a==n:
	print('True')
else:
	print('False')