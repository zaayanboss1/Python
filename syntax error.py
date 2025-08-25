try:
    n1,n2=int(input("enter 2 numbers seperate by comma"))
    result=n1/n2
    print("result is",result)
except ZeroDivisionError as e:
    print("division by 0 is not allowed")
except SyntaxError as s:
    print("comma is missing pls enter the number seperate by comma")
except:
    print("wrong input")
finally:
    print("i'll be excuted no matter what happends")