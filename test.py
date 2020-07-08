edges =[[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
nodes = 7

graph= [[] for _ in range(nodes)]
for e in edges:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

seen =[False]*nodes
dis = [-1]*nodes
fin = [-1]*nodes
parent = [None]*nodes
res = set()
def rec(u,time):
    child = 0
    fin[u] = dis[u] = time
    seen[u] = True
    for v in graph[u]:
        if not seen[v]:
            parent[v] = u
            rec(v,time+1)
            child+=1
            fin[u] = min(fin[u],fin[v])

            if parent[u] == None and child>1:
                res.add(u)
            elif parent[u] != None and fin[v]>=dis[u]:
                res.add(u)
        elif parent[v] != u:
            fin[u] = min(fin[u],dis[v])
    
    return 

rec(0,0)
print(res)