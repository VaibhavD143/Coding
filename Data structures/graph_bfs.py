from collections import deque
def bfs(graph,source):
    visited = [0]*len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            dq = deque([i])
            visited[i] = 1

            while dq:
                elem = deque.popleft(dq)
                # print(elem)
                for node in graph[elem]:
                    if not visited[node]:
                        print(node)
                        visited[node] = 1
                        dq.append(node)
        
graph = [[2],[1,0,3],[0,1,4],[0,1],[2]]
bfs(graph,0)