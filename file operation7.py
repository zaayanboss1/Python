new__file = open('New_file.txt', 'x')
new_file.close()

import os
print("Checking if my_file exist or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hi! Iam penguin and I am 1 yr old.")
my_file.close()

os.remove('Codingal.txt')
os.rmdir('Folder')