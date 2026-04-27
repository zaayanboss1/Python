def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twoSteps = 0
    onstep= 0

    if (stairs>=2):
        twoSteps = ways(stairs-2)

    onstep=ways(stairs-1)
    return twoSteps+onstep
stairs= int(input("Enter number of steps: "))

print("Number to ways to climb: ",ways(stairs))    