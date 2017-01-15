def search(arr,key,lo,hi,flag):
	if flag:
		return mid
      	else:
              	if lo>=len(arr):
			return -1
              	else:
                      	return lo,hi
	mid=(lo+hi)/2
	
	if arr[mid]>key:
		search(arr,key,lo,mid-1)
	elif arr[mid]<key:
		search(arr,key,mid+1,hi)
	elif arr[mid]==key:
		flag=True
	else:
		flage=False


import random
test=sorted([random.randint(1,100) for i in xrange(10)])	

print test,20
print search(test,test[2],0,len(test),None)



