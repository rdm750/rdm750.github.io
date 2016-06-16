# your code goes here
'''
the n-1 bit code, with 0 prepended to each word, followed by
the n-1 bit code in reverse order, with 1 prepended to each word.
Rohit Malgaonkar
'''

def graycode(n):
	if n==1:
		return ['0','1']
	else:
		nbit=map(lambda x:'0'+x,graycode(n-1))+map(lambda x:'1'+x,graycode(n-1)[::-1])
		return nbit

for i in xrange(1,7):
	print graycode(i)

