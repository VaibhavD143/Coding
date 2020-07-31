class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for e,p in zip(edges,succProb):
            graph[e[0]].append((e[1],p))
            graph[e[1]].append((e[0],p))
        maxh = [(-1,start)]
        reach = [0]*n
        reach[start] = 1
        seen = set()
        # n-=1    #n-1 iterations
        while n and maxh:
            prob,node = heapq.heappop(maxh)
            if node in seen:
                continue
            seen.add(node)
            if node == end:
                return reach[end]
            prob = -prob
            for v,p in graph[node]:
                # print(p,prob,reach[v])
                if reach[v] < p*prob:
                    reach[v] = p*prob
                    heapq.heappush(maxh,(-reach[v],v))
            
            n-=1
        return 0
