"""
Intution:
keep two records possible min and max at an position
"""
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mat = [[[0,0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

        mat[0][0][0] = grid[0][0]
        mat[0][0][1] = grid[0][0]
            
        for i in range(1,len(grid)):
            if grid[i][0]<0:
                mat[i][0][0] = grid[i][0]*mat[i-1][0][1]
                mat[i][0][1] = grid[i][0]*mat[i-1][0][0]
            else:
                mat[i][0][0] = grid[i][0]*mat[i-1][0][0]
                mat[i][0][1] = grid[i][0]*mat[i-1][0][1]
        
        for j in range(1,len(grid[0])):
            if grid[0][j]<0:
                mat[0][j][0] = grid[0][j]*mat[0][j-1][1]
                mat[0][j][1] = grid[0][j]*mat[0][j-1][0]
            else:
                mat[0][j][0] = grid[0][j]*mat[0][j-1][0]
                mat[0][j][1] = grid[0][j]*mat[0][j-1][1]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if grid[i][j]<0:
                    mat[i][j][0] = min(grid[i][j]*mat[i-1][j][1],grid[i][j]*mat[i][j-1][1])
                    mat[i][j][1] = max(grid[i][j]*mat[i-1][j][0],grid[i][j]*mat[i][j-1][0])
                else:
                    mat[i][j][0] = min(grid[i][j]*mat[i-1][j][0],grid[i][j]*mat[i][j-1][0])
                    mat[i][j][1] = max(grid[i][j]*mat[i-1][j][1],grid[i][j]*mat[i][j-1][1])

        # for r in mat:
        #     print(r)
        if mat[-1][-1][1]<0:
            return -1
        return mat[-1][-1][1]%(10**9+7)