"""
works for directed graph because in undirected graph we will have
to conisder the parent!
"""
def is_cycle(graph,visited,source):
    cur_stck = [0]*len(graph)
    dq = [source]
    cur_stck[source] = 1

    while dq:
        elem = dq.pop()
        cur_stck[elem] = 1
        visited[elem] = 1
        for node in graph[elem]:
            if not cur_stck[node]:
                dq.append(node)
            else:
                return True
    return False
def driver(graph):
    visited = [0]*len(graph)

    for source in range(len(graph)):
        if not visited[source] and is_cycle(graph,visited,source):
            return True
    return False

graph = [[2],[1,0,3],[0,4,1],[0,1],[2]]
print(driver(graph))