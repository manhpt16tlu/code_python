# Phân tích một số thành thừa số nguyên tố

n = int(input('Nhập số nguyên dương n = '))
x = n
j = 2
print(n,' = ',end='')
while j <= n:
     if n % j == 0:    
          print(j,end ='')
          n //= j
          if n ==1 :
              break
          print('*',end='')
          
     else:
          j += 1
