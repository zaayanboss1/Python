cost=float( input("enter the cost price"))
sp=float(input("enter the selling price"))
profit=0
loss=0
if (sp>cost):
    profit=sp-cost
    print("profit is",profit)
else:
    loss=cost-sp
    print("loss is",loss)