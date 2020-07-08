class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rgraph = [[] for _ in range(len(graph))]
        indegree = [0]*len(graph)
        ss = deque([])        
        for u in range(len(graph)):
            if not graph[u]:
                ss.append(u)
            for v in graph[u]:
                rgraph[v].append(u)
                indegree[u]+=1
        graph = None

        res = []
        while ss:
            node = ss.popleft()
            res.append(node)
            for v in rgraph[node]:
                indegree[v]-=1
                if indegree[v] == 0:
                    ss.append(v)
        return sorted(res)
        