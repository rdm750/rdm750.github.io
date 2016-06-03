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

if __name__ == '__main__':
	max(lstnum)
        remov_dupl(lstnum)
	fibonacci(n)
