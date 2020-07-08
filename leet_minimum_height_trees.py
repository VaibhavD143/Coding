"""
Intution:
we are supposed to find centroid of graph, where node will have minimum height
Keep removing leaf nodes, until there are 2 or 1 nodes left in graph
can be done using set!
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
#         indegree = [0]*n
#         graph = [[] for _ in range(n)]
#         for e in edges:
#             graph[e[0]].append(e[1])
#             graph[e[1]].append(e[0])
#             indegree[e[0]]+=1
#             indegree[e[1]]+=1
#         prev = None
#         curr = [u for u in range(n) if indegree[u]==1 ]
        
#         while curr:
#             prev,curr=curr,[]
            
#             for u in prev:
#                 for v in graph[u]:
#                     indegree[v]-=1
#                     if indegree[v] == 1:
#                         curr.append(v)
#         return prev
        graph = [set() for _ in range(n)]
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        prev = None
        curr = [u for u in range(n) if len(graph[u])==1 ]
        
        while curr:
            prev,curr=curr,[]
            
            for u in prev:
                for v in graph[u]:
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        curr.append(v)
        return prev
            