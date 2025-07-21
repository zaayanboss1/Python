medicalcause=input("Do you have medical cause")
attend=int(input("enter your attendance"))
if medicalcause=="y":
    print("you are allowed")
else:
    if attend>=75:
        print("you are allowed")
    else:
        print("you are not allowed")