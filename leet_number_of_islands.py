"""
https://leetcode.com/problems/number-of-islands/
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt+=1
                    ss = [(i,j)]
                    grid[i][j] = '0'
                    while ss:
                        x,y = ss.pop()
                        for d in dirs:
                            nx = x+d[0]
                            ny = y+d[1]
                            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == '1':
                                ss.append((nx,ny))
                                grid[nx][ny] = '0'
        return cnt

r,c = map(int,input().split())
mat = []
for i in range(r):
    mat.append(input())
vis = [[0]*c for _ in range(r)]
cnt=1
for i in range(r):
    for j in range(c):
        if vis[i][j] == 0 and mat[i][j] != '0':
            stack = [[i,j]]
            while stack:
                x,y = stack.pop()
                vis[x][y] = cnt
                if x-1 >=0 and mat[x-1][y] == '1' and not vis[x-1][y]:
                    stack.append([x-1,y])
                if x+1 < r and mat[x+1][y] == '1' and not vis[x+1][y]:
                    stack.append([x+1,y])
                if y-1 >= 0 and mat[x][y-1] == '1' and not vis[x][y-1]:
                    stack.append([x,y-1])
                if y+1 < c and mat[x][y+1] == '1' and not vis[x][y+1]:
                    stack.append([x,y+1])
            cnt+=1
# for i in mat:
#     print(i)
# for i in vis:
#     print(i)
print(cnt-1)
