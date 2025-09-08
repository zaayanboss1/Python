l=[4,1,8,9,4,5,7,3]
print("original list is",l)
count=0
for i in l:
    count=count+i
average=count/len(l)
print("the sum is",count)
print("the average is",average)
l.sort()
print("the 1st element is",l[0])
print("the last element is",l[-1])