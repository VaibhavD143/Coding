for tc in range(int(input())):
    r,c = map(int,input().split())
    mat = []
    for _ in range(r):
        mat.append(input())
    graph = {}
    indegree = {}
    for i in range(r-1):
        for j in range(c):
            node = mat[i][j]
            pre = mat[i+1][j]
            if node not in indegree:
                indegree[node]=0
            if pre not in graph:
                graph[pre]= set()
            if node == pre:
                continue
            else:
                if node not in graph[pre]:
                    indegree[node]+=1
                    graph[pre].add(node)
    for i in range(c):
        if mat[-1][i] not in indegree:
            indegree[mat[-1][i]]=0
    ss = []
    for i,val in indegree.items():
        if not val:
            ss.append(i)
    res = []
    while ss:
        res.append(ss.pop())
        if res[-1] in graph:
            for v in graph[res[-1]]:
                indegree[v]-=1
                if indegree[v] == 0:
                    ss.append(v)
    if len(res) == len(indegree):
        print("Case #{}: ".format(tc+1)+''.join(res))
    else:
        print("Case #{}: -1".format(tc+1))