n=7
res=''
while n>0:
    res=str(n&1)+res
    n>>=1
    print(res)