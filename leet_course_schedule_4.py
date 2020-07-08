from collections import deque
class Solution:
    def checkIfPrerequisite(self, n: int, pres: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        
        for pre in pres:
            graph[pre[0]].append(pre[1])
        res = []
        for q in queries:
            visited=[False]*n
            ss = deque([q[0]])
            visited[q[0]] = True
            flag = True
            while ss and flag:
                node = ss.popleft()
                # visited[node]=True
                for v in graph[node]:
                    if v == q[1]:
                        res.append(True)
                        flag = False
                        break
                    if not visited[v]:
                        visited[v]=True
                        ss.append(v)
            if flag:
                res.append(False)
        return res
    #from discussion, Floyd-warshall
    def checkIfPrerequisite2(self, n, prerequisites, queries):
        connected = [[False] * n for i in range(n)]

        for i, j in prerequisites:
            connected[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        return [connected[i][j] for i, j in queries]