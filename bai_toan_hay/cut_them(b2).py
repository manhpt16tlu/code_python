"""-Nhập chuỗi và số nguyên dương n
    +nếu độ dài chuỗi > n --> cắt bỏ phía sau chuỗi để độ dài chuỗi = n
    +nếu độ dài chuỗi <= n --> thêm vào đầu chuỗi các kí tự A để đội dài = n
"""

string = input('Nhập 1 chuỗi : ')
while True:
     n = int(input('Nhập số n: ' ))
     if n >= 0 :
          break
print('Chuỗi mới là : ')
if len(string) > n :
     string = string[:n]
else:
    string = string.rjust(n,'A')

print(string)
