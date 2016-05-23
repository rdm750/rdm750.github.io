#prints palindromes with a space
#!/usr/bin/env python
import sys

def palindromes(a,b): 	
	palcount =0
	for i in range(int(a),int(b)+1):
		test = str(i)
		if ''.join(test[::-1]) == test:
			print int(test),' ',
			palcount+=1
	print "\nPalindrome Count: %s"%palcount
if __name__=='__main__':
	if len(sys.argv)!=2:
		palindromes(sys.argv[1],sys.argv[2])
	else:
		print 'run script as script_name.py start end'
