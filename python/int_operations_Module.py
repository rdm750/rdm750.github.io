'''
int operations module
max,remove duplicates,factorial,combinations,
fibonacci,pascal triangle,

rohit malgaonkar

'''
def max(lstnum):
	k=int(lstnum[0])
	for t in lstnum:
		if int(t)>k:
			k=int(t)
	return str(k)
    
def remov_dupl(lstnum):
	newlst=[]
	for strn in lstnum:
		if strn not in newlst:
			newlst.append(strn)
	return newlst


def fibonacci(n):
	if n==0:
		return 0
	if n<2:
		return 1
		
	return fibonacci(n-2) + fibonacci(n-1)

#Fibonacci Modified

def fib(n,a,b):
    if n ==1:
        return a
    elif n==2:
        return b
    return (fib(n-1,a,b))**2 + fib(n-2,a,b)

def fact(k):
    if k<=0:
        return 1
    return k*fact(k-1)
    
def comb(n,r):
    return fact(n)/(fact(r)*fact(n-r))


def pascal(r):
	for k in xrange(0,r+1):
		for c in xrange(0,k+1):
			if k-1>0:
				print comb(k-1,c-1) + comb(k-1,c),
			elif k-1==0 and c==0:
				print comb(k-1,c-1),
		print '\n',

if __name__ == '__main__':
	max(lstnum)
        remov_dupl(lstnum)
	fibonacci(n)
        fib(n,a,b)
        fact(k)
	comb(n,r)
	pascal(r)

