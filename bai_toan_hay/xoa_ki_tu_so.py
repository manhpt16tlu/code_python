#xóa hết kí tự số trong chuỗi
string = input('Nhập chuỗi: ')
i = 0
while i < len(string)  :
    if string[i].isdigit():
          string = string[:i] + string[i+1:]
    else:
         i += 1
print(string)
     
          
