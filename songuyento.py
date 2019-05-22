#kiểm tra số 3nguyên tố
a=2
kt=True
   n=int(input('enter the value of natural number n<>0: '))
   if n>0:
   	break
if n==1:
	print('False')
#1 không là số nguyên tố 
elif n==2:
	print('True')
#2 là số nguyên tố 
else:
    while True:
      if (n%a)!=0:
          a+=1
      elif (n%a)==0:
        break
    if a==n:
    	print('True')
    else:
	    print('False')
    
      



