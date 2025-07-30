n=int(input("enter the number"))
t=n
numlen=0
while t>0:
    numlen=numlen+1
    t=t//10
if numlen>=4:
    numlen=numlen//2
    c=0
    while (n>0):
        r=n%10
        if c==numlen:
              m1=r
        elif  c==numlen-1:
             m2=r
        n=n//10
        c=c+1
    pro=m1*m2
    print("product is",pro)
else:
     print("the number doesn't have 4 digit")
        