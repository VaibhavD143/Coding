class Solution:
    def minCost(self, houses: List[int], rate: List[List[int]], m: int, n: int, target: int) -> int:
        def helper(prev,target,ind):
            if target == -1:
                return float('inf')
            if ind == m:
                if target == 0:
                    return 0
                return float('inf')
            if m-ind<target:
                return float('inf')
            if dp[target][prev][ind]!=-1:
                return dp[target][prev][ind]
            
            if houses[ind] != 0 :
                if houses[ind] == prev:
                    res = helper(prev,target,ind+1)
                else:
                    res = helper(houses[ind],target-1,ind+1)
                dp[target][prev][ind] = res
                return res
            res = float('inf')
            
            for col in range(1,n+1):
                res = min(res,helper(col,target-(prev!=col),ind+1)+rate[ind][col-1])
            # print(target,prev,ind,res)
            dp[target][prev][ind] = res
            return res
        
        dp = [[[-1]*m for _ in range(n+1)] for _ in range(target+1)]
        ans = helper(-1,target,0)
        return ans if ans!=float('inf') else -1

    def minCost1(self, houses: List[int], rate: List[List[int]], m: int, n: int, target: int) -> int:
        
        #prev : previous index color(0-based)
        #ind : current house index
        #rem : remaining number of clusters
        def rec(prev,ind,rem):
            #valid configuration, reached end so no more cost
            if ind == len(houses) and rem == 0:
                return 0

            #invalid configuration, as index is exhausted or rem is negative
            if ind == len(houses) or rem<0:
                return float('inf')
            
            if dp[rem][ind][prev] != -1:
                return dp[rem][ind][prev]
            
            #if already painted house
            if houses[ind] != 0:
                #color matches with previous color then cluster remains same
                if prev == houses[ind]-1:
                    dp[rem][ind][prev] = rec(prev,ind+1,rem)
                else:
                    dp[rem][ind][prev] = rec(houses[ind]-1,ind+1,rem-1)
                return dp[rem][ind][prev]
            
            nonlocal n  #number of colors available
            tres = float('inf')
            #trying all available color for current house and choosing one which gives minimum cost
            for col in range(n):
                if col == prev:
                    t = rate[ind][col]+rec(prev,ind+1,rem)
                else:
                    t = rate[ind][col]+rec(col,ind+1,rem-1)
                tres = min(tres,t)
            dp[rem][ind][prev] = tres
            return tres
        
        dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(target+1)]
        ans = float('inf')
        #as initial house has no previous color
        if houses[0]==0:
            for col in range(n):
                ans = min(ans,rate[0][col]+rec(col,1,target-1))
        else:
            ans = rec(houses[0]-1,1,target-1)
        return ans if ans!=float('inf') else -1