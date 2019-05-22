from tkinter import *#gọi thư viện tkinter
from time import *#hàm delay 
game=Tk()#tạo cửa sổ game 
game.title("KHỦNG LONG")#tên game
cv=Canvas(master=game,width=500,height=500,background='blue')
'''
tạo màn hình game chiều rộng width,chiều cao height,background màu nền'''
cv.pack()#ghim màn hình game vào cửa sổ game 
hcn=cv.create_rectangle(0,0,100,200,fill="red",outline="green")#tạo hcn
text=cv.create_text(200,100,text='hello',fill='black',font=("times",20))
#tạo dòng chữ hello màu đen
cv.update()#lệnh update sau khi tạo hcn
for i in range(0,100):#vòng lặp cho khối hcn di chuyển 100 lần
      cv.move(hcn,0.1,0.1)#di chuyển khối hcn
      cv.move(text,0.5,-0.2)#di chuyển dòng text
      sleep(0.01)#dừng 0.1s để quan sát các khối di chuyển
      cv.update()
game.mainloop()#chạy game