#Rohit Malgaonkar
#40/80 points 
'''
Zalando CodeSprint • 510/ 1478 participants
www.hackerrank.com/rdm750
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
items = int(input())
shelf=map(int,raw_input().split())

for i in xrange(int(input())):
    tup=map(int,raw_input().split())
    k=0
    for t in range(tup[0],tup[1]+1):
        x=shelf[t-1]
        shelf.remove(shelf[t-1])
        shelf.insert(k,x)
        k+=1
    
print ' '.join(map(str,shelf))
