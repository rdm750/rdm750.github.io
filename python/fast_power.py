# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a,b,t = map(int,raw_input().split())

#print int(((a+b)/2)**t) % ((10**9)+7)

def power(x,y):
    res = 1
 
    x = x % ((10**9)+7)
 
    while (y > 0):
        if y & 1:
            res = (res*x) % ((10**9)+7)
        y = y>>1
        x = (x*x) % ((10**9)+7)
    return res

print power((a+b)/2,t)
