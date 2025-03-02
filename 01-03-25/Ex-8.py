'''
Python program to check if the given string is a palindrome

'''
try:
	s = eval(input('Enter any string : '))
	t = s[::-1]
	res = s == t
	if res:
		print(F'{s}  is palindrome')
	else:
		print(F'{s} is not palindrome')
except:
	print('Input Should be string')