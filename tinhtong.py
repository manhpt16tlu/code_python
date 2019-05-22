#tính tổng các số trong mảng 
from array import *
sum=0
arr=array('i',[])
n=int(input('enter the length of the array: '))
for i in range(n):
    x=int(input('enter the next value: '))
    arr.append(x)
    sum+=x

print('tổng các số trong mảng: ',sum)
