def solve(self, A, B, C):
    def rec(src,parent):
        cnt = 0
        nonlocal tot
        for u,c in graph[src]:
            if u != parent:
                child=rec(u,src)
                tot.append(c*child)
                cnt+=child
        return cnt+1
    graph = [[] for _ in range(A)]
    for u,v,c in B:
        graph[u-1].append((v-1,c))
        graph[v-1].append((u-1,c))
    tot = []
    rec(0,-1)
    tot.sort(reverse = True)
    sm=0
    for i in range(C,len(tot)):
        sm+=tot[i]
    return sm

a = []