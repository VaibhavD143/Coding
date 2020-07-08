"""
Converted nodes to 0-indexed from 1-indexed
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for _ in range(n)]
        
        for e in edges:
            graph[e[0]-1].append(e[1]-1)
            graph[e[1]-1].append(e[0]-1)
        seen = [False]*n

        ss = deque([[0,1],None])
        seen[0]=True
        while ss:
            node = ss.popleft()
            if node == None:
                if ss:
                    ss.append(None)
                    t-=1
                    #seconds are finished
                    if t<0:
                        return 0
                continue
            #options current node has
            cnt = sum(1 for v in graph[node[0]] if not seen[v])
            # print(cnt,node,graph[node[0]])
            #converted to 0-index so -1
            if node[0] == target-1:
                #if t is perfect or seconds are left but leaf node, so stays there only
                if t == 0 or (t>0 and cnt==0):
                    return node[1]
                return 0
            #leaf node, to avoid division 0
            if cnt == 0:
                prob = node[1]
            else:
                #probability of child of current node
                prob = node[1]*(1/cnt)
            for v in graph[node[0]]:
                if not seen[v]:
                    ss.append([v,prob])
                    seen[v]=True