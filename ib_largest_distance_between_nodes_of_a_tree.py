"""
Gyaan:
Set recursion limit with resource limit for solution 1
Solution 2:
Find farthest node from root, taking it as one end, find farthest node from there and that's the answer
"""
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, lst):
        graph = [[] for _ in range(len(lst))]
        for i,val in enumerate(lst):
            if val == -1:
                root = i
                continue
            graph[i].append(val)
            graph[val].append(i)
        
        #Solution1, mySolution
        # def dfs(graph,u,visited,state):
            
        #     visited[u]=True
        #     curr=[0,0]
        #     for v in graph[u]:
        #         if not visited[v]:
        #             curr.append(dfs(graph,v,visited,state))
        #     curr.sort()
        #     state[0] = max(state[0],curr[-1]+curr[-2])
            
        #     return curr[-1]+1
        
        # visited = [False]*len(lst)
        # state = [0]
        # dfs(graph,root,visited,state)
        # return state[-1]
        
        #Solution2, Editorial
        ss = deque([root,None])
        dist1 = 0
        start = root
        visited = [False]*len(lst)
        while ss:
            u = ss.popleft()
            if u == None:
                if ss:
                    ss.append(None)
                    dist1+=1    
                continue
            start = u    
            visited[u]=True
            for v in graph[u]:
                if not visited[v]:
                    ss.append(v)
        
        ss = deque([start,None])
        res = 0
        end = start
        visited = [False]*len(lst)
        while ss:
            u = ss.popleft()
            if u == None:
                if ss:
                    ss.append(None)
                    res+=1    
                continue
            end = u    
            visited[u]=True
            for v in graph[u]:
                if not visited[v]:
                    ss.append(v)
        return res