class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        def rec(a,b):
            if a==len(A):
                return len(B)-b
            if b==len(B):
                return len(A)-a
            if dp[a][b] != -1:
                return dp[a][b]
            if A[a] == B[b]:
                dp[a][b] = rec(a+1,b+1)
            else:
                dp[a][b] = 1+min(rec(a+1,b),rec(a,b+1),rec(a+1,b+1))
            return dp[a][b]
        dp= [[-1]*(len(B)+1) for _ in range(1+len(A))]
        # return rec(0,0)
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j]=j
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]        
                