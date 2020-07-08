"""
Intution : 
Version 3 : More than slow
Find all the vallies and put it into `block`
pre[l][r] = maximum profit between l-r blocks
dp[k][ind] = maximum profit from at most k transactions, starting index `ind` of block

Version 2:
Memory limit exceeded and TLE also
dp[i][j] = max profit with i transactions till jth day
dp[i][0] = 0 and dp[0][i] = 0
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
to understand `maxPrev`
Version 3: optimisation of Version 2
k>=len(prices) to handle TLE
dp0 dp1 to handle Memory
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices or not k:
            return 0
        
        if k>=len(prices)//2:
            res = 0
            for i in range(1,len(prices)):
                res+=prices[i]-prices[i-1] if prices[i]>prices[i-1] else 0
            return res
        
        dp0 = [0]*len(prices)
        dp1 = dp0[:]
        
        for i in range(1,k+1):
            maxPrev = -prices[0]
            for j in range(1,len(prices)):
                dp1[j] = max(dp1[j-1],maxPrev+prices[j])
                maxPrev = max(maxPrev,dp0[j-1]-prices[j])
            if dp0[-1]==dp1[-1]:
                return dp1[-1]
            dp0,dp1=dp1,dp0
            
        return dp0[-1]
        
        
        # dp = [[0]*len(prices) for _ in range(k+1)]
        # for i in range(1,k+1):
        #     maxPrev = -prices[0]
        #     for j in range(1,len(prices)):
        #         dp[i][j] = max(dp[i][j-1],maxPrev+prices[j])
        #         maxPrev = max(maxPrev,dp[i-1][j-1]-prices[j])
        #     if dp[i-1][-1]==dp[i][-1]:
        #         return dp[i][-1]
        # return dp[-1][-1]


        if not prices or k==0:
            return 0
        def rec(ind,k):
            
            if k==0:
                return pre[ind][-1]
            if dp[k][ind] != None:
                return dp[k][ind]
            res = 0
            for i in range(ind,len(block)-k):
                res = max(res,pre[ind][i]+rec(i+1,k-1))
            dp[k][ind] = res
            return res
        
        block = []
        left= 0
        for i in range(1,len(prices)):
            if prices[i-1]>prices[i]:
                if i-1!=left:
                    block.append((prices[left],prices[i-1]))
                left = i
        if left!=len(prices)-1:
            block.append((prices[left],prices[-1]))
        
        if k>=len(block):
            return sum(r-l for l,r in block)
        if len(block) == 0:
            return 0
        if len(block) == 1:
            return block[0][1]-block[0][0]
        
        dp = [[None]*len(block) for _ in range(k)]
        pre = [[0]*len(block) for _ in range(len(block))]
        for r in range(len(block)-1,-1,-1):
            max_p = block[r][1]
            pre[r][r] = block[r][1]-block[r][0]
            
            for l in range(r-1,-1,-1):
                max_p = max(max_p,block[l][1])
                pre[l][r] = max(pre[l+1][r],max_p-block[l][0])

        return rec(0,k-1)