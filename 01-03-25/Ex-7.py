'''
Python program to count the total number of digits in a number.

'''
try:
	n = int(input('Enter a number : '))
	count = 0
	if n == 0:
		count = 1
	else:
		while n > 0:
			count += 1
			n = n // 10
	print(count)

except:
	print('Input should ba an integer')
