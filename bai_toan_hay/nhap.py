n=int(input("nhap n so : "));

dem=0;
for i in range (2,n+1):
    m=0;
    for j in range (1,i+1):                  
        if(i%j==0):
           m=m+1;
    if(m==2):
       print (i)           
