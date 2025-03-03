'''
Print the first 10 natural numbers using for loop.
'''
try:
	n = int(input('Enter number : ' ))
	sum=0
	for i in range(1,n+1):
		sum+=i
	print(F'{n} natural numbers sum : {sum}')
		
except:
	print('Input should be an integer')
