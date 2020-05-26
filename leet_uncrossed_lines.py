class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        def rec(ind1,ind2):
            if ind1==len(A) or ind2 == len(B):
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            dp[ind1][ind2] = max(rec(ind1+1,ind2),rec(ind1,ind2+1))
            if A[ind1] == B[ind2]:
                dp[ind1][ind2] = max(dp[ind1][ind2],1+rec(ind1+1,ind2+1))
            return dp[ind1][ind2]
        dp = [[-1]*len(B) for _ in range(len(A))]
        return rec(0,0)