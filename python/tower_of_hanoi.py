#tower of hanoi python
# a=source; b= intermediate;c=destination
#move n-1 disk from a to b; move n from a to c;move n-1 disk from b to c

def hanoi(n,s,i,d):
	if n >0:
		hanoi(n-1,s,d,i)
		print "disk "+str(n)+" is moved from "+str(s)+" to "+str(d)
		hanoi(n-1,i,s,d)
hanoi(7,'a','b','c')

