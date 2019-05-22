#sapxep
from array import *
arr = array('i',[])
arr1=[]#tạo một list rỗng 
n = int(input('enter the length of the array:'))#nhap độ dài của mảng
for i in range(n):
	      x =int(input('enter the next value: '))#nhập giá trị của phần tử
	      arr.append(x)
	      arr1.append(x)
print('mang vua nhap:')
print(arr)
arr1.sort()#sắp xếp tăng dần
print('mang da sap xep tang dan:')
print(arr1)
arr1.sort(reverse=True)#sắp xếp giảm dần
print('mang da sap xep giam dan:')
print(arr1)

