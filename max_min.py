from array import *
arr=array('i',[])
n=int(input('enter the length of array:'))
for i in range(n):
	   x=int(input('enter the next value:'))
	   arr.append(x)  
max=arr[0]
min=arr[0]
for i in range(n):
    if arr[i]>max:
                 max=arr[i]
    if arr[i]<min:
		         min=arr[i]
print('gia tri lon nhat cua mang: ',max)
print('gia tri nho nhat cua mang: ',min)
