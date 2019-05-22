"""tính tổng các số chia hết cho k trong [1,n]"""

while True:
    n = int(input('Nhập số nguyên dương n > 1:  '))
    if n >1 :
         break

k = int(input('Nhập số nguyên k:  '))
s = 0

for i in range(1,n+1):
    if i % k == 0:
        s+=i

print('Tổng các số chia hết cho ',k ,' từ 1 đến ',n,' là: ',s)
