'''
Rohit Malgaonkar
Zalando CodeSprint • 510/ 1478 participants
www.hackerrank.com/rdm750

Choosing the right pair of shoes to purchase with an article of clothing is not an obvious decision. Given the purchase frequency for shoes that were previously purchased with an item, can you help a customer by showing them the  most popular shoes (in popularity order)?
25/25 points

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT'
L = map(int,raw_input().split())
K,M,N=L[0],L[1],L[2]
#print K,M,N
has={}
for i in xrange(N):
    data= int(raw_input())
    if data in has: 
        has[data] +=1
    else:
        has[data]=1
has = sorted(has, key=has.__getitem__,reverse=True)
for k in xrange(K):
    print has[k]
