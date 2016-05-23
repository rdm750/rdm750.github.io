'''
This prints unique substrings for a given string
pass by cli in unix mac osx
unique_substring.py ababba

'''
# your code goes here
#test= 'abab'
#for i in range(len(test)):
#	for k in range(len(test)-i):
#		print test[i:i+k+1]
import sys

def uniq_substring(test):
	lista=[]
	[lista.append(test[i:i+k+1]) for i in range(len(test)) for k in range(len(test)-i) if test[i:i+k+1] not in lista and test[i:i+k+1][::-1] not in lista]
	print lista
	print "Numer of Uniq Substrings: %s"%len(lista)

if len(sys.argv)!=1:
	uniq_substring(sys.argv[1])
else:
	print 'run script as script_name.py Given_String.'
	print 'Example: python uniq_substring.py rohit'
	uniq_substring('rohit')
	uniq_substring('abab')	
