
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