from array import *

arr = array('i',[])

n = int(input('Nhập số phần tử của mảng: '))
for i in range(n):
   x = int(input('Nhập phần tử tiep theo: '))
   arr.append(x)
 


for i in range(n):
  print(arr[i])
