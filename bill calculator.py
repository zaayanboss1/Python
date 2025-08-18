def total_bill(bill,tip):
    total=bill*(1+0.1*tip)
    total=round(total,2)
    print("please pay",total)
total_bill(150,20)
