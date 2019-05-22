#    tìm các số chia hết cho 7 nhưng ko  phải bội
#    của 5 trong đoạn 2000-->3200
#    các số thu được in thành chuỗi trên 1 dòng

print('các số cần tìm là: ')
for i in range(2000 , 3200):
     if (i % 7 == 0) and (i % 5 != 0):
          print(i,',' ,end =' ')
