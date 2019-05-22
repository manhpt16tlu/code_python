"""Nhập số nguyen a,b in ra phân số tối giản của a/b"""

a = int(input('Nhập tử số  a nguyên =  '))
while True:
    b = int(input('Nhập mẫu số  b nguyên =  '))
    if b != 0 :
         break
if a > b:
     x = b
else:
     x = a


if (a % b == 0):
     print('Phân số tối giản của ',a,'/',b,' là: ',a//b,'/1')
else:
     for i in range(2,abs(x)):
          if a % i ==0 and b % i == 0:
               a = a // i
               b = b // i
     if a < 0 and b < 0:
          print(-a,'/',-b)
     else:
          print(a,'/',b)
     
