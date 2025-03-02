'''
 Python program that accepts a word from the user and reverses it.

'''
try:
	s = eval(input('Enter a String : '))
	res = s[::-1]
	print(F'Before reverse : {s}')
	print(F'After reverse : {res}')
except:
	print('Input should be string')