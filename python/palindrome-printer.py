#prints palindromes with a space
import sys
palcount =0
for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
	test = str(i)
	if ''.join(test[::-1]) == test:
		print int(test),' ',
		palcount+=1
print "\nPalindrome Count: "+str(palcount)
