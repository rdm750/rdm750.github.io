grid=\
'''
3 5
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
3
0 0 2 4
0 3 2 3
1 1 1 3

'''
print grid
print 'find and print the minimum possible weight of a path connecting them.'
ans=\
'''
1
1
18
'''
print ans

# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

def initDis(distances,row,col):
    for R in xrange(row):
        for C in xrange(col):
            distances[(R,C)]=-1
    return distances

def djikstra(graph,start,n,dist,distances):
    visited,hq=set(),[]
    #distances=[-1]*n
    
        
    distances[start]=dist[start]
    heapq.heappush(hq,(distances[start],start))    
    while len(hq)!=0:
        (dis,vertex)=heapq.heappop(hq) 
        if vertex not in visited:
            visited.add(vertex)
            if distances[vertex]==-1:
                distances[vertex]=dis
            for v in graph[vertex]:
                if distances[v]==-1 or distances[v] > dis+dist[v]:
                    distances[v] = dis+dist[v]
                    heapq.heappush(hq,(distances[v],v))
    return distances

                
row,col=map(int,raw_input().split())
graph=dict()

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
            
dist=dict()      
distances=dict()

for r in xrange(row):
    for ro,co in enumerate(map(int,raw_input().split())):
        dist[(r,ro)]=co
        distances[(r,ro)]=-1
    for c in xrange(col):
        for x,y in adjacency:
            if 0 <= (r + x) < row and 0 <= c + y < col:
                graph.setdefault((r,c),set()).add((r + x, c + y))

    
query=int(input())

for qu in xrange(query):
    a,b,c,d = map(int,raw_input().split())
    start=(a,b)
    end=(c,d)
    res=djikstra(graph,start,len(graph),dist,distances)
    print res[end]
    distances=initDis(distances,row,col)

    
    

