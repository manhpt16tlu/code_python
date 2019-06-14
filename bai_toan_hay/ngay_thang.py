""" nhập tháng và năm,in ra số ngày trong tháng """

def day(m,y) :
     if y % 4 == 0 and y % 100 != 0 :
          if  m == 2 :
               return 29
     else :
          if m == 2 :
               return 28
     if m <= 7 :
          if m % 2 == 0 :
               return 30
          else :
               return 31
     elif m > 7 :
          if m % 2 == 0 :
               return 31
          else :
               return 30



while True:
    month = int(input('Nhập tháng :  '))
    if month >= 1 and month <= 12 :
        break

while True:
    year = int(input('Nhập năm :  '))
    if year > 0 :
        break

print('Tháng ',month ,' năm ', year,' có ',day(month,year),'ngày ')




