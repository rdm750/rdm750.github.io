# your code goes here
'''
the n-1 bit code, with 0 prepended to each word, followed by
the n-1 bit code in reverse order, with 1 prepended to each word.
Rohit Malgaonkar
'''
import os
import sys

F=[[]]*100

def graycode(n):
	if n==1:
		F[n]=['0','1']
		return ['0','1']
	else:
		if F[n]!=[]:
			return F[n]
		else:
			nbit=map(lambda x:'0'+x,graycode(n-1))+map(lambda x:'1'+x,graycode(n-1)[::-1])
			F[n]=nbit	
		return nbit

print map(int,graycode(int(sys.argv[1])))
print F

