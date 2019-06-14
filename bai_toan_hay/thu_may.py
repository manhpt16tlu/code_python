#nhập ngày tháng năm in ra hôm nay là thứ mấy
from ngay_thu_may import *
def thu_may(x):
     y = x % 7
     z = ['monday','tuesday','wesnesday','thurday','priday','saturday','sunday']
     return z[y]
          
    
day = int(input('Nhập ngày: '))
month = int(input('Nhập tháng: '))
year = int(input('Nhập năm: ' ))
nhuan(year)
t = ngay(day,month,year)
print('hôm nay là  : ',thu_may(t))







