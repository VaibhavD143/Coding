"""
Intution:
same as word ladder 1, create a graph from dictionary
now apply bfs as shortes path is required and it is unweighted
once we find a path, that's the last level
"""

from collections import defaultdict
from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        dictV = list(set(dictV))
        source = dictV.index(start)
        dest = dictV.index(end)
        
        graph = [set() for _ in range(len(dictV))]
        l_word = len(start)
        
        ha = defaultdict(list)
        for ind,word in enumerate(dictV):
            for i in range(l_word):
                tword = word[:i]+'_'+word[i+1:]
                ha[tword].append(ind)
        # print(ha)
        for word,lst in ha.items():
            for u in range(len(lst)):
                for v in range(u+1,len(lst)):
                    graph[lst[u]].add(lst[v])
                    graph[lst[v]].add(lst[u])
        
        # print(dictV)
        # for i,r in enumerate(graph):
        #     print(i,dictV[i],r)
    
        res= []
        visited = [False]*len(graph)
        ss = deque([[source],None])
        visited[source] = True
        while ss:
            path = ss.popleft()
            # print(path)
            if path == None:
                # print("ss",ss)
                if res or not len(ss):
                    break
                else:
                    ss.append(None)
                continue
            node = path[-1]
            visited[node] = True
            if node == dest:
                res.append(path)
                break
            for v in graph[node]:
                if not visited[v]:
                    ss.append(path+[v])
                    
            
        while ss:
            path = ss.popleft()
            if path == None:
                break
            if path[-1] == dest:
                res.append(path)
        return [[dictV[i] for i in r] for r in res]