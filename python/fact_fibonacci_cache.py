F=[-1]*20
R=[-1]*20

def fact(n):
    if n==0:
        R[n]=1
        return 1
    else:
        k=R[n] 
        if k!=-1:
	    print '--'	
            return k
        
        k=n*fact(n-1)
        R[n]=k
        
        return R[n]
    
def fib(n,a,b):
    if n ==1:
        F[n]=a
        return a
    elif n==2:
        F[n]=b
        return b
    ret=F[n]
    if ret!=-1:
	print '--'
        return ret
    
    ret=(fib(n-1,a,b))**2 + fib(n-2,a,b)
    F[n]=ret
    return F[n] 


#arr=map(int,raw_input().split())
arr=[0,1,10]
print'*'*10
print fib(arr[2],arr[0],arr[1])
print '*'*10
print filter(lambda x:x!=-1,F)
print '*'*10
[fact(h) for h in xrange(10)]

print filter(lambda x:x!=-1,R)
print '*'*10
print fact(5)
print '*'*10
