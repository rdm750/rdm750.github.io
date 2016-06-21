'''
int operations module
max,remove duplicates,factorial,combinations,
fibonacci,pascal triangle,binary search sorted array,
return integer pairs matching a difference from an array
quicksort(lomato partition scheme implement)
bitflip,insertion sort,

rohit malgaonkar

'''
from math import *

def is_prime(x):
    if x<2:
        return False
    for n in range(2,x):
        if x%n==0:
            return False

    else:
        return True

def prime_factors(n):
    factors=set()
    for i in xrange(2, int(sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n /= i
    if n != 1:
        factors.add(n)
    return factors


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

#binary search
def search(arr,key,mind,maxd):
	if maxd < mind:
		return -1
	else:
		index = (maxd+mind)/2
		if arr[index] > key:
			return search(arr,key,mind,index-1)
		elif arr[index] < key:
			return search(arr,key,index+1,maxd)
		else:
			return index
#recursion quicksort partition
def pivot_start_partition(ar):
    if len(ar)>1:
        p=ar[0]
        eq,left,right=[],[],[]
        for i in ar:
            if i > p:
                right.append(i)
            elif i < p:
                left.append(i)   
            else:
                eq.append(i)
        listn=pivot_start_partition(left)+pivot_start_partition(eq)+pivot_start_partition(right)
        for t in listn: 
            print t,
        print ''  
        return listn
    else:
        return ar
# implemented https://en.wikipedia.org/wiki/Quicksort
#Lomuto_partition_scheme
def quicksort(ar,lo,hi):
    if lo < hi: 
        p= partition(ar,lo,hi)
        print ' '.join(map(str,ar))
        quicksort(ar, lo, p-1)
        quicksort(ar, p + 1, hi)
        
    else:
        return

def partition(A,lo,hi):
    pivot = A[hi]
    i = lo        # place for swapping
    for j in xrange(lo,hi):
        if A[j] <= pivot:
            x=A[i]
            A[i]=A[j]
            A[j]=x
            i+=1
    x=A[i]
    A[i]=A[hi]
    A[hi]=x
    left,right=[],[]

    return i

# insertion sort
def insertionSort(arr):    
    for i in xrange(1,len(arr)):
        j=i
        
        while (j >0 and arr[j-1]>arr[j]):
            arr[j]^=arr[j-1]  
            arr[j-1]^=arr[j]
            arr[j]^=arr[j-1] 
            j-=1
        print ' '.join(map(str,arr))    
   






def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    answer = 0
    arr={}
    for i in a:
        arr[i]=1
    for r in arr:
        try:
            if arr[r+k]==1:
                answer+=1
        except:
            pass

    return answer

#return 32 bit integer bit flipped xor by all 1s to flip the bits. 1^1=0, 0^1=1

def bitflip(n):
    return n^((1<<32)-1)

if __name__ == '__main__':
	max(lstnum)
        remov_dupl(lstnum)
	fibonacci(n)
        fib(n,a,b)
        fact(k)
	comb(n,r)
	pascal(r)
        search(arr,key,min,max)
        pivot_start_partition(ar)
	pairs(a,k)
	quicksort(ar,lo,hi)
	bitflip(n)
        insertionSort(ar)

