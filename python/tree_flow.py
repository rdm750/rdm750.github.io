'''
tree_flow_input_19.txt
tree_flow_output_19.txt

Recall that a tree is an undirected, connected acyclic graph. We have a weighted tree,T , with n vertices; let dist(v,u) be the total sum of edge weights on the path between nodes u and v       

Let's consider all the matrices, , such that:
Au,v = -Av,u   (reversed flow = negative forward flow)
0<= |Au,v|<= distu,v
sum,i=1 to i=n Au,i = 0 for each u!=1 and u!=n
 
We consider the total value of matrix  to be:
sum,i=1 i=n A1,i

Calculate and print the maximum total value of  for a given tree,T .


passed all test cases! (python solution)
max score on dfs: 80/80 bfs:56/80 djikstra:48/80
applied iterative (non-recursive) dfs on the graph (passes all tests, 80/80) applied bfs on the graph (timeouts 35-48 tests,passes 41 &42. score: 56/80) applied djikstra on the graph (timeouts 33-47 tests,runtime error on last 48th test. score: 48/80)
solved after contest 101 hack June 2016

#https://www.hackerrank.com/rdm750

101 Hack June 2016 701/ 1979 participants
BlackRock CodeSprint 476/ 3211 participants
Zalando CodeSprint  510/ 1478 participants


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

print 'copy and paste input from tree_flow_input_19.txt'

def dfs(graph, start,dlength,EdgeDis):
    visited, stack = set(), [start]
    distances = [-1] * dlength
    distances[int(start) -1]=0
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for v in graph[vertex]:
                if distances[int(v)-1]==-1:
                    distances[int(v)-1]=distances[int(vertex)-1]+min(EdgeDis[tuple([vertex,v])])
            stack.extend(graph[vertex] - visited)
    return filter(lambda x:x!=-1,distances)

'''   
def bfs(graph, start,dlength,EdgeDis):
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
                    distances[int(v)-1]=distances[int(vertex)-1]+min(EdgeDis[tuple([vertex,v])])
            queue.extend(graph[vertex] - visited)
    #print distances,'*'*10,visited
    return filter(lambda x:x!=-1,distances)
'''    
'''
def djikstra(graph,start,n,EdgeDis):
    visited,hq=set(),[]
    distances=[-1]*n
    distances[start-1]=0
    heapq.heappush(hq,(distances[int(start) -1],start))    
    while len(hq)!=0:
        (dis,vertex)=heapq.heappop(hq) 
        if vertex not in visited:
            visited.add(vertex)
            if distances[vertex-1]==-1:
                distances[vertex-1]=dis
            for v in graph[vertex]:
                if distances[int(v)-1]==-1 or distances[int(v)-1] > dis+min(EdgeDis[tuple([vertex,v])]):
                    distances[int(v)-1]=dis+min(EdgeDis[tuple([vertex,v])]) 
                    heapq.heappush(hq,(distances[int(v)-1],int(v)))
    return distances
'''
n=int(input())
graph=dict()
EdgeDis=dict()
for r in xrange(n-1):
    a,b,c=map(int,raw_input().split())
    #make graph and EdgeDistances
    graph.setdefault(a,set()).add(b)
    graph.setdefault(b,set()).add(a)
    EdgeDis.setdefault(tuple([a,b]),list()).append(c)
    EdgeDis.setdefault(tuple([b,a]),list()).append(c)
#print graph 
#print EdgeDis
sol = dfs(graph,1,n,EdgeDis)
sol2 = dfs(graph,n,n,EdgeDis)
print min(sum(sol),sum(sol2))
#print min(sol,sol2)
#print min(sum([0 if k==-1 else int(k) for k in sol]) ,  sum([0 if k==-1 else int(k) for k in sol2]) )
#sol = ['-1' if k=='inf' else str(k) for k in sol]  
#print ' '.join(sol)

        

