#in ra k số cuối cùng của n giai thua
def giai_thua(x):
     if x == 0:
          return 1
     else:
          return x * giai_thua(x - 1)

def dem_so():
     string = str(giai_thua(n))
     print(string[len(string)-k:])

#chương trình chính
n = int(input('Nhập n = '))
print(n ,'!= ')
print(giai_thua(n))
k = int(input('Nhập số k = '))
dem_so()




