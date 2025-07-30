word= input("enter the word")
c=input("enter your the character")
i=0
count=0
while i<len(word):
    if(word[i]==c):
        count=count+1
    i=i+1
print("the total number of times",c,"occured",count)