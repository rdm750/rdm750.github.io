'''
Zalando CodeSprint • 510/ 1478 participants
www.hackerrank.com/rdm750
Rohit Malgaonkar
32/60 points
'''
i# Enter your code here. Read input from STDIN. Print output to STDOUT
Nabc=map(int,raw_input().split())
order=0
for r in xrange(int(input())):
    lista=map(str,raw_input().split(','))
    #each item only once
    once=[]
    ful=0
    for k in lista:
        if k=='A':
            if len(once)<3 and Nabc[0] >0:
                Nabc[0]-=1
                ful+=1
                once.append(1)
        elif k=='B':
            if len(once)<3 and Nabc[1] >0:
                Nabc[1]-=1
                ful+=1
                once.append(1)
        elif k=='C':
            if len(once)<3 and Nabc[2] >0:
                Nabc[2]-=1
                ful+=1
                once.append(1)
    if ful==len(lista):
        order+=1

print order
        
       
            
    
