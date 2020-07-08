"""
Intution:
applying BFS
consider node again if cost to reach node is lesser than current cost, step will always be greater than current as we are doing BFS
"""
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        graph = [[] for _ in range(n)]
        for edge in flights:
            graph[edge[0]].append([edge[1],edge[2]])
        cost = [float('inf')]*n
        ss = deque([[src,-1,0]])
        # cost[src] = 0
        while ss:
            node = ss.popleft()
            if node[0] == dst:
                continue
            if node[1] == K:
                continue
            for v,c in graph[node[0]]:
                if cost[v]>node[2]+c:
                    cost[v] = node[2]+c
                    ss.append([v,node[1]+1,node[2]+c])
        return cost[dst] if cost[dst]!=float('inf') else -1