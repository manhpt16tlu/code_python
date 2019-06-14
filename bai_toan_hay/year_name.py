""" nhập 1 năm từ bàn phím ,in ra tên của năm đó  """

def chi(x):
     if x % 12 == 8 :
         return ' thìn'
     elif x % 12 == 9 :
        return ' tị'
     elif x % 12 == 10 :
        return ' ngọ'
     elif x % 12 == 11 :
        return ' mùi'
     elif x % 12 == 0 :
        return 'thân'
     elif x % 12 == 1 :
        return 'dậu'
     elif x % 12 == 2 :
        return ' tuất'
     elif x % 12 == 3 :
        return ' hợi'
     elif x % 12 == 4 :
        return ' tí'
     elif x % 12 == 5 :
        return ' sửu'
     elif x % 12 == 6 :
        return ' dần'
     elif x % 12 == 7 :
        return ' mão'

def can(x):
     if x % 10 == 9 :
        return 'Kỷ'
     elif x % 10 == 0 :
        return 'Canh'
     elif x % 10 == 1 :
        return 'Tân'
     elif x % 10 == 2 :
        return 'Nhâm'
     elif x % 10 == 3 :
        return 'Quý'
     elif x % 10 == 4 :
        return 'Giáp'
     elif x % 10 == 5 :
        return 'Ất'
     elif x % 10 == 6 :
        return ' Bính'
     elif x % 10 == 7 :
        return 'Đinh'
     elif x % 10 == 8 :
        return 'Mậu'

while True:
     year = int(input('Nhập năm :  '))
     if year > 0 :
          break
print(year,'là năm ',can(year)+chi(year))

