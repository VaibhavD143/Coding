"""
Intution:
dp[j][diff] : stores length of progression including jth index with difference diff
Gyaan:
- Faster, second solution is same but we are looping differently and accessing dp[j] all together
which will save time because it will use cached 
- In first looping it is changing rows, slower
- avoid defaultdict if possible, very expensive
"""
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        dp = [{} for _ in range(len(A))]
        
        res = 2
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                diff = A[i]-A[j]
                dp[j][diff] =dp[i].get(diff,1)+1
                # dp[j][diff] =max(dp[j][diff],dp[i][diff]+1)   not reuires max() as it will be the same number, because of difference 
                res = max(res,dp[j][diff])
        return res
        
        # for j in range(1,len(A)):
        #     for i in range(j):
        #         diff = A[i]-A[j]
        #         dp[j][diff] =dp[i].get(diff,1)+1
        #         res = max(res,dp[j][diff])
        # return res