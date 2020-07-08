
def topological(graph,visited,source,res):
    
    for node in graph[source]:
        if not visited[node]:
            topological(graph,visited,node,res)
    visited[source] = 1
    res.append(source)
    
graph = [[1,2,3],[4],[1,3],[4],[],[6],[]]
visited = [0]*len(graph)
res = []
for i in range(len(graph)):
    if not visited[i]:
        topological(graph,visited,i,res)
print(res[::-1])

from collections import deque
def topSort(graph):
    indegree = [0]*len(graph)
    for u in range(len(graph)):
        for v in graph[u]:
            indegree[v]+=1
    
    ss = deque([])
    
    for i,val in enumerate(indegree):
        if val == 0:
            ss.append(i)
    # visited = [False]*len(graph)
    res = []
    while ss:
        node = ss.popleft()
        # visited[node] = True
        res.append(node)
        for v in graph[node]:
            indegree[v]-=1
            if indegree[v] == 0:
                ss.append(v)
    return res if len(res)==len(graph) else -1
