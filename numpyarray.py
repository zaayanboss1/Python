import numpy as np

a = np.arrange(9,dtype=np.float_).reshape(3,3)
print('First array : ')
print(a)
print('\n')

b=np.array([10,10,10])
print('Second array: ')
print(b)
print('\n')

print('add the two arrays: ')
print(np.add(a,b))
print('\n')

print('subtract the two arrays: ')
print(np.subtract(a,b))
print('\n')

print('Divide the two arrays: ')
print(np.divide(a,b))
print('\n')