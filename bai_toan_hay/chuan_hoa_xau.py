#chuẩn hóa xâu

string = input('Nhập một chuỗi từ bàn phím: ')


string = string.lstrip() # xóa dấu cách thừa bên trái
string = string.rstrip()#xóa dấu cách thừa bên phải
string = string.title() #viết hoa chữ cái đầu mỗi từ

while string.find('  ') > 0:           #tìm và thay thế 
     string = string.replace('  ',' ')
print(string)

