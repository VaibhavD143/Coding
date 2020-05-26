"""
Intution:
just do dfs on a graph
"""

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        ha = defaultdict(list)
        isRoot = [True]*n
        for i in edges:
            ha[i[0]].append(i[1])
            ha[i[1]].append(i[0])
        # dist = [0]*n
        # print(ha)
        def rec(ha,u,visited):
            cnt=0
            visited[u]=True
            for v in ha[u]:
                if not visited[v]:
                    # print(u,v)
                    tmp = rec(ha,v,visited)
                    if hasApple[v] or tmp:
                        cnt+=tmp+2
            return cnt
        visited=[False]*n
        return rec(ha,0,visited)