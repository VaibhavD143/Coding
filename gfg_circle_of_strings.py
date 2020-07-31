"""
Intution:
Make graph of characters considering first and last character
Find if there is eulerian circuit or not
Euler circuit:
1) indegree and outdegree of vertex is same for all vertices
2) graph is single strongly connected component
"""
def helper(lst):

    graph = [[] for _ in range(26)]
    indegree = [0]*26
    
    for i,w in enumerate(lst):
        graph[ord(w[0])-ord('a')].append(ord(w[-1])-ord('a'))
        indegree[ord(w[-1])-ord('a')]+=1

    # print(indegree)
    # print(lst)
    # print(graph)
    for i,o in zip(indegree,map(len,graph)):
        if i!=o:
            return 0
    src = ord(lst[0][0])-ord('a')
    if isSC(graph,src):
        return 1
    return 0
    
def dfs(graph,src,seen,path):
    seen[src] = True
    for v in graph[src]:
        if not seen[v]:
            dfs(graph,v,seen,path)
    path.append(src)

def transposeGraph(graph):
    tgraph = [[] for _  in range(len(graph))]
    for i,lst in enumerate(graph):
        for j in lst:
            tgraph[j].append(i)
    return tgraph

def isSC(graph,src):
    seen = [False]*len(graph)
    path = []
    
    dfs(graph,src,seen,path)
    # print(path)
    for i,s in enumerate(seen):
        if s == False and graph[i]:
            return 0
    
    tgraph = transposeGraph(graph)
    # print(tgraph)
    # print("res : ",end=" ")
    seen = [False]*len(tgraph)
    dfs(tgraph,path[0],seen,[])
    for i,s in enumerate(seen):
        if s == False and tgraph[i]:
            return 0
    return 1

for _ in range(int(input())):
    n = int(input())
    lst = input().split()
    print(helper(lst))