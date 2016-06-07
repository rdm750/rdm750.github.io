'''
Rohit Malgaonkar
Zalando CodeSprint • 510/ 1478 participants
www.hackerrank.com/rdm750

24/40 points
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
listb=[]
for i in xrange(int(input())):
    lista = map(int,raw_input().split())
    if lista[0] == 1:
        tup=(lista[1],lista[2])  #P,T
        listb.append(tup)
    elif lista[0] == 2:
        T=lista[1]
        x=-1
        listc=listb
        for k in listc:
            if k[1] >= T-59:
                if x<=k[0]:
                    x=k[0]
                    #print x,
            elif k[1] < T-59:
                listb.remove(listb[listb.index(k)])
        #print listb,T,x
        if x!=0:
            print x
        else:
            print -1
        

    


