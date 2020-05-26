class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0
        maxCap = max(A)
        dp = [float('inf')]*(maxCap+1)
        dp[0]=0
        for i in range(len(B)):
            for ind in range(B[i],len(dp)):
                dp[ind] = min(dp[ind-B[i]]+C[i],dp[ind])
        res=0
        for i in A:
            res+=dp[i]
        return res
                