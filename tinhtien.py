#tính tiền taxi
''' Số km ≤ 1 giá 15000đ
1 < số km ≤ 5 giá 13500đ
Số km > 5 giá 11000đ
Nếu số km > 120 km sẽ được giảm 10% trên tổng số tiền.
'''

n=int(input('nhap so km: '))
if n<=1:
	 s=15000
	 print('giá tiền là: ',s)
elif 1<n<=5:
	 s=15000+(n-1)*13500
	 print('giá tiền là: ',s)
elif 5<n<=120:
	 s=15000+4*13500+(n-5)*11000
	 print('giá tiền là: ',s)
else:
     s=(15000+4*13500+(n-5)*11000)*0.9
     print('giá tiền là: ',s)


