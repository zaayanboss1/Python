def summ(n):
    if n <=0:
        return  0 
    return n+summ(n-1)
print("REcursive sum (n=5):",summ(5))