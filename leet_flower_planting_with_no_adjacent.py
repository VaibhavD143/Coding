"""
Intution:
As there can be maximum 3 edges to node
so greedy n-coloring can work
greedy n-coloring works for d+1 colors, where d is max degree of a node in graph.
greedy won't gaurantee minimum color usage
"""
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        for e in paths:
            graph[e[0]-1].append(e[1]-1)
            graph[e[1]-1].append(e[0]-1)
        res = [-1]*N
        for i in range(N):
            res[i] = ({1,2,3,4}-{res[j] for j in graph[i]}).pop()
        return res