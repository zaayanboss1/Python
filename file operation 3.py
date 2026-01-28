file1 = open('zaayan.txt','r')
file2 = open('zaayan.txt','W')

for line in file1.readlines():
    if not (line,startswith('coding')):
        print(line)


        file2.write(line)


file.1(close)
file.2(close)