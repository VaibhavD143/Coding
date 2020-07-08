"""
Intution:
Get all the rooten oranges as starting node of BFS and do BFS considering them as level-0
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dist = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        ss = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dist[i][j]=0
                    ss.append((i,j))
        ss.append(None)
        d = 0
        res =0
        while ss:
            node = ss.popleft()
            if not node:
                if ss:
                    ss.append(None)
                    d+=1
                continue
            x,y=node[0],node[1]
            
            for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and dist[nx][ny]>d+1 and grid[nx][ny] == 1:
                    ss.append((nx,ny))
                    dist[nx][ny] = d+1
            res = max(res,dist[x][y])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and dist[i][j]==float('inf'):
                    return -1
        return res