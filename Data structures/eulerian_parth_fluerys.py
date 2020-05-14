
"""
If there 0 or 2 odd degree vertices then there is a eulerian path or cycle exist
start from one of the odd vertex if there is

first check wether path exist or not
traverse in dfs manner from there
try to avoid bridge edge
remove edge:
1: if the only adjacent vertex
2: not bridge
    - that is, removing edge won't change the reachability of the number of vertices
"""

def isEulerian(graph):
    #returns node number if path exist (to start dfs from there), otherwise -1
    cnt = node =0
    for i in range(len(graph)):
        if len(graph[i])&1:
            cnt+=1
            node = i
    if cnt ==0 or cnt ==2:
        return node
    return -1

def dfs_count(graph,source):
    stack = [source]
    visited = [0]*len(graph)
    cnt = 0
    visited[source] = 1
    while stack:
        elem = stack.pop()
        cnt+=1
        for i in graph[elem]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
    return cnt

def is_valid(graph,u,v):
    #only adjacent
    if len(graph[u]) == 1:
        graph[u].remove(v)
        graph[v].remove(u)
        return True
    #2 not bridge
    cnt1 = dfs_count(graph,u)
    graph[u].remove(v)
    graph[v].remove(u)
    cnt2 = dfs_count(graph,u)
    if cnt1>cnt2:
        graph[u].append(v)
        graph[v].append(u)
        return False
    return True

def eulerianPath(graph,source):
    # stack = [source]
    curr = source
    flag = 1
    path = [source]
    while flag:
        # node = stack.pop()
        flag = 0
        for node in graph[curr]:
            if is_valid(graph,curr,node):
                # stack.append(node)
                curr = node
                print(curr,"current")
                print(graph)
                path.append(curr)
                flag = 1
                break
    return path
def driver(graph):
    source = isEulerian(graph)
    if source == -1:
        return False
    print(source)
    
    path = eulerianPath(graph,source)

    print(path)

graph = [[1,2],[0,2],[0,1,3],[2]]
driver(graph)