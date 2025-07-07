height=float(input("enter the height"))
weight=float(input("enter the weight"))
hm=(height/100)
bmi=(weight/hm**2)
if bmi<=18.4:
    print("you are underweight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are overweight")
elif bmi<=34.9:
    print("you are obese")
else:
    print("you are severely obese")


