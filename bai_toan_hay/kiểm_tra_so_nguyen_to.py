"""Đếm các số nguyên tố trong đoạn [1,n]"""

#hàm kiểm tra số nguyên tố
def kiem_tra(x):
    j = 2
    while True:
         if x % j != 0:
              j += 1
         else:
               break
    if j == x:
          return True
    else:
          return False


#chương trình chính
while True:
    n = int(input('Nhập số nguyên dương n:  '))
    if n > 0:
         break
     
count = 0
for i in range(2,n+1):
    if kiem_tra(i):
         count += 1

print('Có ',count,' số nguyên tố trong đoạn [1,',n,'] ')
     
