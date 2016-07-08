banner='''
You are given a matrix with  rows and  columns of cells, each of which contains either  or . Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. The connected and filled (i.e. cells that contain a ) cells form a region. There may be several regions in the matrix. Find the number of cells in the largest region in the matrix.
input
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

output
5


'''
print banner


# Enter your code here. Read input from STDIN. Print output to STDOUT
def initDis(distances,row,col):
    for R in xrange(row):
        for C in xrange(col):
            distances[(R,C)]=-1
    return distances

def dfs(graph,start,n,dist,distances):
    visited, stack = set(), [start]
    distances[start]=dist[start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if distances[vertex]==-1 and dist[vertex]>0:
                distances[vertex]=dist[vertex]
            for v in graph[vertex]:
                if distances[v]==-1 and dist[v]==1:
                    distances[v] = distances[vertex]+dist[v]

            stack.extend(graph[vertex] - visited)
    #print visited
    return filter(lambda x:x>0,distances.values())

row=int(input())
col=int(input())

graph=dict()

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
            
dist=dict()      
distances=dict()
lstart=[]

for r in xrange(row):
    for ro,co in enumerate(map(int,raw_input().split())):
        dist[(r,ro)]=co
        distances[(r,ro)]=-1
        if co == 1:
            lstart.append((r,ro))
for r in xrange(row):            
    for c in xrange(col):
        for x,y in adjacency:
            if 0 <= (r + x) < row and 0 <= c + y < col:
                if dist[(r+x,c+y)]>0:
                    graph.setdefault((r,c),set()).add((r + x, c + y))  
                else:
                    graph.setdefault((r,c),set())   
 
ans=-1
#print graph
for start in lstart:
    res=dfs(graph,start,len(graph),dist,distances)
    ans=max(ans,len(res))
    distances=initDis(distances,row,col)
    
print ans

#print distances    
