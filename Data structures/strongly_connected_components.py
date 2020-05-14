
def transpose_graph(graph):
    n_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            n_graph[j].append(i)
    return n_graph

def driver(graph):
    visited = [0]*len(graph)
    dfs = []
    for i in range(len(graph)):
        if not visited[i]:
            dq = [i]
            visited[i] = 1

            while dq:
                elem = dq.pop()
                dfs.append(elem)
                for node in graph[elem]:
                    if not visited[node]:
                        dq.append(node)
                        visited[node] = 1
    print(dfs)
    
    t_graph = transpose_graph(graph)
    print(t_graph)

    visited = [0]*len(graph)
    res=[]
    for i in dfs:
        if not visited[i]:
            dq = [i]
            visited[i] = 1
            t_res = []
            while dq:
                elem = dq.pop()
                t_res.append(elem)
                for node in t_graph[elem]:
                    if not visited[node]:
                        dq.append(node)
                        visited[node] = 1
            res.append(t_res)
    return res

graph = [[2,3],[0],[1],[4],[]]
print(driver(graph))
# print(transpose_graph(graph))