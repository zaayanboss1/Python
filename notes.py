amount=int(input("ENTER THE AMOUNT"))
note1=amount//1000
note2=(amount%1000)//500
note3=((amount%1000)%500)//100
note4=(((amount%1000)%500)%100)//10
note5=((((amount%1000)%500)%100)%10)//5
print("total number of thousand note are",note1)
print("total number of 500 note are",note2)
print("total number of 100 note are",note3)
print("total number of 10 note are",note4)
print("total number of 5 note are",note5)