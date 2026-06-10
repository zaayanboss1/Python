def equilibriumPoint(arr):
    leftSideSum=0
    rightSideSum=0
    n=len(arr)

    for i in range (n):
        leftSideSum=0
        rightSideSum=0

    for j in range(i):
        leftSideSum+= arr[j]

    for j in range(i+1,n):
        rightSideSum+=arr[j]

    if leftSideSum == rightSideSum:
        return i
    return -1

arr = [-4,6,2,0,5,3,2]
print("Element : ",arr[equilibriumPoint(arr)])