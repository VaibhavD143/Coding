class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def add(lst1,lst2):
            for i,v in enumerate(lst2):
                lst1[i]+=v
                
        def dfs(root,parent,labels):
            cnt = [0]*26
            cnt[ord(labels[root])-ord('a')]=1
            for v in graph[root]:
                if v != parent:
                    tcnt = dfs(v,root,labels)
                    add(cnt,tcnt)
            res[root] = cnt[ord(labels[root])-ord('a')]
            return cnt
        
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        res = [-1]*n
        dfs(0,-1,labels)
        return res