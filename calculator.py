def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("the list of operation is")
print("1:add")
print("2:substract")
print("3:multiply")
print("4:divide")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
choice=int(input("enter your choice"))
if choice==1:
    print("the sum is",add(n1,n2))
elif choice==2:
    print("the difference is",sub(n1,n2))
elif choice==3:
    print("the product is",multiply(n1,n2))
elif choice==4:
    print("the quotient is",divide(n1,n2))
else:
    print("wrong choice")



