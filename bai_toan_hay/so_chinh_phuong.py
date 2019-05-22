#kiểm tra số chính phương
from math import sqrt as can
while True:
  n = int(input('nhap so n > 0 =  '))
  if n > 0 :
          break
x = int(can(n))

if x ** 2 == n:
  print('True')
else:
  print('False')
