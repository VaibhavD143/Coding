"""
Intution:
linearly it will be TLE
so we do binary jump also known as binary lifting
self.graph[i][j] stores (1<<i)th parent of node j
so we do binary jumps whenever needed
"""
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
#         self.par = parent
#         self.graph = [[] for _ in range(n)]
#         for i in range(1,n):
#             self.graph[parent[i]].append(i)
        
#         self.anc= [[] for _ in range(n)]
#         ss=deque([0])
#         while ss:
#             node = ss.popleft()
#             for v in self.graph[node]:
#                 self.anc[v].extend([node]+self.anc[node])
#                 ss.append(v)
        step = 17
        self.graph = [parent[:]]
        for s in range(1,step):
            lst = [-1]*n
            for i in range(n):
                if self.graph[s-1][i] !=-1:
                    lst[i]  = self.graph[s-1][self.graph[s-1][i]]
            self.graph.append(lst[:])        

    def getKthAncestor(self, node: int, k: int) -> int:
        step = 16
        while k and node!=-1:
            if k>=(1<<step):
                k-=(1<<step)
                node = self.graph[step][node]
                step-=1
            else:
                step-=1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)