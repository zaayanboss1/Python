try:
    a=int(input("enter a number"))
    print("the number enter is",a)
except ValueError as ex:
    print("the number enter by you isn't correct",ex)