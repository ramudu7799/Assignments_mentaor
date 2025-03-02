'''
Python program to calculate the sum of all the odd numbers within the given range.

'''
try:
	n = int(input('Enter a number : '))
	oddSum = 0 
	for i in range(1,n+1,2):
		oddSum += i
	print(oddSum)
except ValueError:
	print('Input Should be an integer')
