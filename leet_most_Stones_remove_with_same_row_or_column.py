"""
Intution:
Find number of components in graph, each component will miss one point
DFS can be used to find #connected components
1 DUS : if point clash with any previous point on same column and/or same row then union then in single component
2 DUS : to avoid most checks and distiguish rows and columns, add 10000 to column number, so will work directly
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # parent = list(range(len(stones)))
        parent = {}
        def find(i):
            if i!=parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            if i not in parent:
                parent[i]=i
            if j not in parent:
                parent[j]=j
            p1 = find(i)
            p2 = find(j)
            parent[p1] = p2
        
#         cols = {}
#         rows = {}
#         for i,e in enumerate(stones):
#             if e[1] not in cols:
#                 cols[e[1]] = i
#             else:
#                 union(i,cols[e[1]])
            
#             if e[0] not in rows:
#                 rows[e[0]] = i
#             else:
#                 union(i,rows[e[0]])
#         tot = set()
#         for i in range(len(parent)):
#             tot.add(find(i))
#         return len(stones)-len(tot)
        for x,y in stones:
            union(x,10000+y)
        return len(stones)-len({find(i) for i in parent})