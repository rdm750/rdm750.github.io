'''
passed all test cases
Solution: Python
hackerrank maximum perimeter triangle
Given  sticks of lengths , use  of the sticks to construct a non-degenerate triangle with the maximum possible perimeter. Then print the lengths of its sides as  space-separated integers in non-decreasing order.

Rohit Malgaonkar

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
L = sorted(map(int,raw_input().split()),reverse=True)
per=()
peri=0
if n > 2:
    for i in xrange(len(L)-1):
        if i <= len(L)-3:
            if L[i]+L[i+1] > L[i+2] and L[i]+L[i+2]> L[i+1] and L[i+2]+L[i+1]> L[i]:

                if peri < L[i]+L[i+1]+L[i+2]:
                    peri= L[i]+L[i+1]+L[i+2]
                    per =(L[i],L[i+1],L[i+2])

if peri ==0:
    print -1
else:
    for t in sorted(per):
        print t,


