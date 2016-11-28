Max,Min = None,None

#divide and conquer for max min finder in array

def maxmin(arr,lo,hi):
	if lo==hi:
		Max,Min=arr[lo],arr[hi]
		return Max,Min
	elif hi==lo+1:
		if arr[hi]>arr[lo]:
			Max,Min=arr[hi],arr[lo]
		else:
			Max,Min=arr[lo],arr[hi]
		return Max,Min
	m=(lo+hi)/2
	maxl,minl=maxmin(arr,lo,m)
	maxr,minr=maxmin(arr,m+1,hi)
	if minl < minr:
		Min=minl
	else:
		Min=minr
	if maxl<maxr:
		Max=maxr
	else:
		Max=maxl
	return Max,Min

import random
test=[random.randint(1,100) for i in xrange(10)]

print test

print maxmin(test,0,len(test)-1),max(test),min(test)
print (maxmin(test,0,len(test)-1))==(max(test),min(test))







