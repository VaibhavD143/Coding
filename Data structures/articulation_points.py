
def ap(graph,source,desc,low,is_ap,visited,parent):
    global time    
    desc[source] = time
    low[source] = time
    time+=1
    visited[source] = 1
    children = 0
    for node in graph[source]:
        if not visited[node]:
            
            children+=1
            parent[node]=source
            ap(graph,node,desc,low,is_ap,visited,parent)
            
            low[source] = min(low[source],low[node])

            if parent[source] == None and children>1:
                is_ap[source] = True
            
            if parent[source] != None and desc[source] <= low[node]:
                is_ap[source] = True
            
        elif parent[source] != node:
            low[source] = min(low[source],desc[node])            

def driver(graph):
    visited = [0]*len(graph)
    desc = [0]*len(graph)
    low = [0]*len(graph)
    is_ap = [0]*len(graph)
    parent = [None]*len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            print(i)
            ap(graph,i,desc,low,is_ap,visited,parent)
    print(is_ap,desc,low)
    # for i in range(len(graph)):
    #     if is_ap[i]:
    #         print(i)
    
time = 0
graph = [[1],[2],[3],[]]
driver(graph)