num=int(input("enter the number"))
sum=0
temp=num

while (temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if (num==sum):
    print("its an armstrong number")
else:
    print("its not an armstrong number")
