#https://www.hackerrank.com/challenges/bfsshortreach
test=\
'''
breadth first search: short reach solution Hackerrank
input
2
4 2
1 2
1 3
1
3 1
2 3
2

output
6 6 -1
-1 6

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

print test

def bfs(graph, start,dlength):
    visited, queue = set(), [start]
    distances = [-1] * dlength
    distances[int(start) -1]=0
    #print distances
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            #print vertex
            for v in graph[vertex]:
                #print v,
                #if int(v)!=int(start):
                if distances[int(v)-1]==-1:
                    distances[int(v)-1]=distances[int(vertex)-1]+6
            queue.extend(graph[vertex] - visited)
    #print distances,'*'*10,visited
    return distances
testcases=int(input())

for s in xrange(testcases):
    graph=dict()
    NM=map(int,raw_input().split())
    for k in xrange(NM[1]):
        tup = map(str,raw_input().split())
        graph.setdefault(tup[0],set()).add(tup[1])
        graph.setdefault(tup[1],set()).add(tup[0])
        
    for x in xrange(1,NM[0]+1):
        if str(x) not in graph.keys():
            graph.setdefault(str(x),set())
    
    start=str(input())    
    #print graph,start
    sol = [str(j) for j in bfs(graph,start,NM[0]) if j !=0]
    print ' '.join(sol)


  

    
