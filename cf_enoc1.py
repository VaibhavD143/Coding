level = 17
for _ in range(int(input())):
    n,q = map(int,input().split())
    lst = list(map(int,input().split()))
    graph = {i:[] for i in lst}
    xor = {i:0 for i in lst}
    for _ in range(n-1):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    def dfs(node,prev,l,val):
        par[node][0] = prev
        lev[node] = l
        visited[node]=True
        xor[node] = val^node
        for v in graph[node]:
            if not visited[v]:
                dfs(v,node,l+1,xor[node])
    visited = {i:False for i in lst}
    par = {i:[-1]*level for i in lst}
    lev = {i:0 for i in lst}
    dfs(lst[0],-1,0,0)
    def parent():
        for l in range(1,level):
            for i in lst:
                if par[i][l-1] != -1:
                    par[i][l] = par[par[i][l-1]][l-1]
    parent()
    def lca(u,v):
        # print(u,v)
        if lev[u]>lev[v]:
            u,v=v,u
        diff = lev[v]-lev[u]
        # print(diff)
        for i in range(level,-1,-1):
            if diff>=(1<<i):
                v = par[v][i]
                diff-=(1<<i)
        # print(u,v)
        if u==v:
            return u
        while par[v][0] != par[u][0]:
            v = par[v][0]
            u = par[u][0]
        return par[u][0]


    for _ in range(q):
        u,v = map(int,input().split())
        LCA = lca(u,v)
        print(xor[u]^xor[v]^LCA)