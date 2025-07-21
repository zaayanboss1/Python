units=int(input("enter number of unit consume"))
if units<50:
    amount=units*2.60
    surcharge=25
elif units<100:
    amount=130+((units-50)*3.25)
    surcharge=35
elif units<150:
    amount=130+162.5+((units-100)*5.26)
    surchare=45
else:
    amount=130+162.5+526+((units-150)*5.26)
    surcharge=55

total=amount+surcharge
print("the total amount is",total)