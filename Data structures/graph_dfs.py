
def dfs(graph):
    visited = [0]*len(graph)
    res = []
    for i in range(len(graph)):
        if not visited[i]:
            dq = [i]
            visited[i] = 1

            while dq:
                elem = dq.pop()
                res.append(elem)
                for node in graph[elem]:
                    if not visited[node]:
                        dq.append(node)
                        visited[node] = 1
    print(res)        
graph = [[1,2],[2],[1]]
dfs(graph)