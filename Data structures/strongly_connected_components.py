"""
Working
"""
from collections import deque
def transpose_graph(graph):
    n_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            n_graph[j].append(i)
    return n_graph

def fillOrder(graph,u,stack,visited):
    visited[u]=True
    for v in graph[u]:
        if not visited[v]:
            fillOrder(graph,v,stack,visited)
    stack.append(u)



def driver(graph):
    visited = [False]*len(graph)
    dfs = []
    #this is not just a dfs, we add node to the stack after it finishes 
    for i in range(len(graph)):
        if not visited[i]:
            fillOrder(graph,i,dfs,visited)
    print(dfs)
    
    t_graph = transpose_graph(graph)
    print(t_graph)

    visited = [False]*len(graph)
    res=[]
    # for i in reversed(dfs):
    while dfs:
        u=dfs.pop()
        if not visited[u]:
            dq = [u]
            visited[u] = True
            t_res = []
            while dq:
                elem = dq.pop()
                t_res.append(elem)
                for node in t_graph[elem]:
                    if not visited[node]:
                        dq.append(node)
                        visited[node] = True
            res.append(t_res)
    return res

graph = [[2,3],[0],[1],[4],[]]
print(driver(graph))
# print(transpose_graph(graph))