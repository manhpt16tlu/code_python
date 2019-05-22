#tính giai thừa 1 số nhập từ bàn phím
def giai_thua(gt):
  if  gt == 0:
     return 1
  else:
     return gt * giai_thua(gt - 1)

    
while True:
  n = int(input('Nhập số nguyên dương n : '))
  if n >= 0 :
    break

print(giai_thua(n))

  
       
