from array import *
"""---định nghĩa hàm---"""
#hàm nhập mảng
def nhap_mang():
     for i in range(n):
          print('Nhập phần tử   thứ ',i + 1,' : ',end  =  ' ')
          x = int(input())
          arr.append(x)
          
#xuất mảng
def xuat_mang():
  for i in arr:
          print(i,end = '  ')
     
#hàm sắp xếp tăng dần
def tang_dan():
      for i in range(n - 1):
          for j in range(i + 1,n):
               if arr[i] > arr[j]:
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
      xuat_mang()
      
#hàm sắp xếp giảm dần
def giam_dan():
     for i in range(n - 1):
          for j in range(i + 1,n):
               if arr[i] < arr[j]:
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
     xuat_mang()
     
#hàm xóa phần tử thứ k trong mảng
def xoa():
     k = int(input('Nhập giá trị của k: '))
     for i in range(k-1,n-1):
          arr[i] = arr[i+1]
     for i in range(n-1):
          print(arr[i],end =' ')

#hàm chèn gía trị x vào vị trí k
def chen():
     arr.append(0)
     k = int(input('Nhập vị trí k: '))
     x = int(input('Nhập giá trị x cần chèn: '))





     
"""---chương trình chính---"""
n = int(input('Nhập số phần tử của mảng: '))
arr = array('i',[])
nhap_mang()
xuat_mang()
print('\n')

#xoa()
#tang_dan()
#giam_dan()

