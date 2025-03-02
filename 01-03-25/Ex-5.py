'''

Python program to print a multiplication table of a given number


'''
try:
	n = int(input('Enter a number : '))
	for i in range(1,11):
		print(F'{n} x {i} = {n * i}')
except:
	print('Input should be an integer')