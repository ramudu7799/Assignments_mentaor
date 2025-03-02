
'''
Python program to calculate the sum of all numbers from 1 to a given number.

'''
try:
	n = int(input('Enter a number '))
	res = 0
	if n < 1:
		print('Please Enter a number at least 2')
	else:
		for i in range(1,n+1):
			res += i
	print(res)
except ValueError:
	print('Input should be an ineteger')