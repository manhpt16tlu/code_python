#bài toán với mảng 1 chiều


arr = [] #khai báo list rỗng
length = int(input('Nhập số phần tử của mảng: '))

for i in range(length):
     print('Nhập phần tử thứ ',i+1,': ',end = ' ')
     x = int(input())
     arr.append(x)

print('Mảng bạn vừa nhập là: ',end = '')
for i in arr:
     print(i,end = ' ')


print('\n')
#sắp xếp mảng tăng dần(mặc định)
arr.sort()
for i in arr:
  print(i,end = ',')


