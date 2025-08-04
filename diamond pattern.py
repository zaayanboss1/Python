rowsize = int(input("Enter the number of rows: "))

# Determine half (for both even and odd)
if rowsize % 2 == 0:
    half = rowsize // 2
else:
    half = rowsize // 2 + 1

# Upper half
space = half - 1
for i in range(1, half + 1):
    for j in range(space):
        print(" ", end="")
    space -= 1
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()

# Lower half
space = 1
for i in range(1, half):
    for j in range(space):
        print(" ", end="")
    space += 1
    num = 1
    for j in range(2 * (half - i) - 1):
        print(num, end="")
        num += 1
    print()
