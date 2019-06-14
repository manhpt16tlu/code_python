string  = input('Nhập chuỗi: ')
m = input('Nhập chuỗi hoặc kí tự muốn xóa: ')
while True:
     t = string.find(m)
     if t == -1 :
          break
     else:
          string = string[:t] + string [t + len(m):]

print(string)
