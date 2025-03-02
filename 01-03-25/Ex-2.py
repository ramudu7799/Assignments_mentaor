
'''
Python program to print all the even numbers within the given range.

'''


try:
	n = int(input('Enter a number : '))
	if n < 1:
		print('Please enter a number greater than or equal to 1')
	else:
		for i in range(1,n+1):
			if i % 2 == 0:
				print(i)
except ValueError:
	print('Input should be an integer')