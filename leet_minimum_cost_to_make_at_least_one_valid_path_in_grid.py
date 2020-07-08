"""
Intution:
Apply dfs to find all the reachable node from current node, those are at level 0 with cost 0
then we apply bfs on them, which cost us 1 so they are at level 1 with cost 1
and so on
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # cost = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        # cost[-1][-1] = 0
        # dirs = [[0,-1,1],[-1,0,3],[1,0,4],[0,1,2]]
        # ss = deque([(len(grid)-1,len(grid[0])-1)])
        # while ss:
        #     x,y = ss.popleft()
        #     for addx,addy,d in dirs:
        #         nx,ny = x+addx,y+addy
        #         if 0<=nx<len(grid) and 0<=ny<len(grid[0]):
        #             if d == grid[nx][ny] and cost[nx][ny]>cost[x][y]:
        #                 cost[nx][ny] = cost[x][y]
        #                 ss.append((nx,ny))
        #             elif cost[nx][ny]>1+cost[x][y]:
        #                 cost[nx][ny] = 1+cost[x][y]
        #                 ss.append((nx,ny))
        # return cost[0][0]
        seen = [[False]*len(grid[0]) for _ in range(len(grid))]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(x,y):
            if not (0<=x<len(grid) and 0<=y<len(grid[0]) and seen[x][y] ==False):
                return
            bfs.append((x,y))
            seen[x][y] = True
            dfs(x+dirs[grid[x][y]-1][0],y+dirs[grid[x][y]-1][1])
        bfs=[]
        bfs2 = [(0,0)]
        cost = 0
        dfs(0,0)
        while bfs:
            if seen[-1][-1] == True:
                return cost
            cost+=1
            bfs,bfs2 = [],bfs
            for x,y in bfs2:
                for d in dirs:
                    dfs(x+d[0],y+d[1])
        
                