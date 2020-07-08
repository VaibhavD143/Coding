class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], inform: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i,par in enumerate(manager):
            if i == headID:
                continue
            graph[par].append(i)
        res=0
        def dfs(u):
            
            tres = 0
            for v in graph[u]:
                tres = max(tres,inform[u]+dfs(v))
            
            return tres
        
        return dfs(headID)