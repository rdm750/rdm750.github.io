'''
fair ration from hackerrank contest hourrank-9

'''

#!/bin/python

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

loaf=0
for i in range(len(B)-1):
    if B[i]%2!=0:
        B[i]+=1
        loaf+=1
        if i!=len(B)-1:
            B[i+1]+=1
            loaf+=1
        
k=0        
for i in B:
    if i%2==0:
        k+=1
if k!=len(B):
    print 'NO'
else:
    print loaf
