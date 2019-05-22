#in ra n số nguyên tố đầu tiên,sử dụng sàng số nguyên tố

from math import sqrt as can
while True:
    n = int(input('Nhập n = '))
    if n > 0:
        break

arr = []
for i in range(n+1):
    arr.append(True)

for i in range(2,int(can(n))+1):
    if arr[i] == True:
         for j in range(2*i,n+1,i):
              arr[j] = False

for i in range(2,n+1):
     if arr[i] == True:
          print(i,end='  ')



