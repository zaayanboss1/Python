file = open("zaayan.txt","r")
counter = 0 
contemt= file.read()
Colist = content.split("\n")

for i in Colist:
    if i:
        counter +=1

print("This is the number of lines in the file")
print(Counter)