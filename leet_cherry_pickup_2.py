"""
Intution:
Just bruit force it,
explore every damn posibilities
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # res = grid[0][0]+grid[0][-1]
        # ha= {
        #     0:{(0,len(grid[0])-1):res}
        # }
        # dirs = [-1,0,1]
        # for i in range(1,len(grid)):
        #     ha[i]=defaultdict(int)
        #     for c1,c2 in ha[i-1]:
        #         for r1 in dirs:
        #             for r2 in dirs:
        #                 nc1 = c1+r1
        #                 nc2 = c2+r2
        #                 if 0<=nc1<len(grid[0]) and 0<=nc2<len(grid[0]) and nc1 != nc2:
        #                     ha[i][(nc1,nc2)] = max(ha[i][(nc1,nc2)],ha[i-1][(c1,c2)]+grid[i][nc1]+grid[i][nc2])
        #     del ha[i-1]
        # return max(ha[len(grid)-1].values())
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == m: return 0
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if nc1 >= 0 and nc1 < n and nc2 >= 0 and nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))
            return ans + cherries
        
        return dfs(0, 0, n - 1)