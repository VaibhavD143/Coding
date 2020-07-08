"""
Intution:
- graph is actual representation and while using it swap the co-ordinates, because x-axis is column in matrix and y-axis is rows
- from given circles, first invalidate all the cells which comes under the circle area
        - using `n` as there can be a case where overlapping of two circle in one end can stop iteration till opposite end
- then do the normal bfs/dfs to reach destination like normal problem!
"""


import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, x, y, N, R, A, B):
        graph = [[1]*(x+1) for _ in range(1+y)]
        
        def invalidate(x,y,n):
            
            ss=[(x,y)]
            dirs=[[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
            while ss:
                # print(ss)
                px,py = ss.pop()
                # if px>=0 and px<len(graph[0]) and py>=0 and py<len(graph):
                    
                #     if graph[py][px] != n:
                        # print(px,py,math.sqrt((x-px)**2+(y-py)**2))
                if math.sqrt((x-px)**2+(y-py)**2) <=R:
                    graph[py][px] = n
                    for d in dirs:
                        if 0<=px+d[0]<len(graph[0]) and 0<=py+d[1]<len(graph) and graph[py+d[1]][px+d[0]]!=n:
                            ss.append((px+d[0],py+d[1]))
                    
        for i in range(len(A)):
            invalidate(A[i],B[i],-i-1)

        if graph[0][0]!=1:
            return "NO"
        ss = [(0,0)]
        graph[0][0]=0
        dirs=[[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        while ss:
            px,py = ss.pop()
            for d in dirs:
                if 0<=px+d[0]<len(graph[0]) and 0<=py+d[1]<len(graph) and graph[py+d[1]][px+d[0]]==1:
                    graph[py+d[1]][px+d[0]] = 0
                    ss.append((px+d[0],py+d[1]))
                
        if graph[-1][-1]==0:
            return "YES"
        return "NO"
                
                
                
                
                
                
                
                
                