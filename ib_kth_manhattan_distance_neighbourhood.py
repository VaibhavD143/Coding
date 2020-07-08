"""
Intution:
kth manhattan distance can be derived from k-1 manhattan distance!
"""
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        
        dp= [[0]*(2+len(B[0])) for _ in range(2+len(B))]
        tmp= [[0]*(2+len(B[0])) for _ in range(2+len(B))]
        #for k = 0
        for i in range(len(B)):
            for j in range(len(B[0])):
                dp[i+1][j+1] = B[i][j]
        
        for _ in range(1,A+1):
            for i in range(len(B)):
                for j in range(len(B[0])):
                    tmp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1],dp[i+1][j],dp[i+2][j+1],dp[i+1][j+2])
            # dp = [r[:] for r in tmp]
            dp,tmp = tmp,dp
        
        # for k in range(len(dp)):
        #     print("k : ",k)
        #     for r in dp[k]:
        #         print(r)
        
        for i in range(len(B)):
            for j in range(len(B[0])):
                B[i][j] = dp[i+1][j+1]
        return B
        
        #TLE
        # dp= [[[0]*(2+len(B[0])) for _ in range(2+len(B))] for _ in range(A+1)]
        # #for k = 0
        # for i in range(len(B)):
        #     for j in range(len(B[0])):
        #         dp[0][i+1][j+1] = B[i][j]
        
        # for k in range(1,A+1):
        #     for i in range(len(B)):
        #         for j in range(len(B[0])):
        #             dp[k][i+1][j+1] = max(dp[k-1][i+1][j+1],dp[k-1][i][j+1],dp[k-1][i+1][j],dp[k-1][i+2][j+1],dp[k-1][i+1][j+2])
        
        # # for k in range(len(dp)):
        # #     print("k : ",k)
        # #     for r in dp[k]:
        # #         print(r)
        
        # for i in range(len(B)):
        #     for j in range(len(B[0])):
        #         B[i][j] = dp[-1][i+1][j+1]
        # return B