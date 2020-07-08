class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # def rec(n,s):
        #     if n==1:
        #         return 1 if 0<=s<10 else 0
        #     if s<0:
        #         return 0
        #     if dp[n][s]!= -1:
        #         return dp[n][s]
            
        #     cnt = 0
        #     for i in range(10):
        #         cnt+=rec(n-1,s-i)
        #         cnt%=1000000007
        #     dp[n][s] = cnt
        #     return cnt
        if A==1:
            return 1 if 1<=B<10 else 0
        
        dp = [[0]*(B+1) for _ in range(A+1)]
        
        # for i in range(1,10):
        #     res+=rec(A-1,B-i)
        #     res%=1000000007
        # return res
        #for digit 1-9 , only 1 way possible
        for i in range(1,min(10,len(dp[0]))):
            dp[1][i] = 1
        #any sum can be possible with adding last 10 sum(including current value, as 0 is allowed)
        for i in range(2,len(dp)):
            for j in range(1,len(dp[0])):
                #looping over last 10,i.e. s=11 2+9=s ,3+8=s,4+7=s ...11+0=s
                for k in range(max(1,j-9),j+1):
                    dp[i][j]+=dp[i-1][k]
                dp[i][j]%=1000000007
        return dp[-1][-1]
            
        
        