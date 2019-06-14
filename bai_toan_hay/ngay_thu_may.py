"""nhập ngày tháng năm và in ra ngày thứ bao nhiêu trong năm"""
from math import ceil

# kiểm tra năm nhuận
def nhuan(y):
     if y % 4 == 0 and y % 100 != 0:
          return True
     else :
          return False
#in ra ngày thứ bao nhiêu trong năm
def ngay(d,m,y):
    global s
    s = 0
    i = 1
    while i < m :
             if i == 2:
                  if nhuan(y) :
                       s+= 29
                  else:
                       s+= 28
             elif i in [1,3,5,7,8,10,12] :
                       s += 31
             elif i in [4,6,9,11] :
                       s += 30
             i += 1
    return s + d

"""#in ra tuần thứ bao nhiêu trong năm
def tuan(d):
     print('hôm nay là tuần thứ : ',end ='')
     print(ceil((s+d)/7))"""
     
"""day = int(input('Nhập ngày: '))
month = int(input('Nhập tháng: '))
year = int(input('Nhập năm: ' ))
nhuan(year)
ngay(day,month,year)
tuan(day)"""



