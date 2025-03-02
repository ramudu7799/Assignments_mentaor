
'''
Python program to check if a given number is an Armstrong number

'''





import math
try:
	n = eval(input('Enter a +ve enter : '))
	if(n > 0):
		t = n
		m = n
		res = 0
		count = 0
		while m > 0:
			count += 1
			m = m // 10
		while n > 0:
			r = n % 10
			res = res + math.pow(r,count)
			n = n // 10
		if res == t:
			print(F'{t} is a armstrong number')
		else:
			print(F'{t} is not a armstrong number')
	else:
		print('Input should be  +ve an integer')
except:
	print('Input should be an integer')



		 
		 