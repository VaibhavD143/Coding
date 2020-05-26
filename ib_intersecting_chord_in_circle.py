"""
Intution:
when we draw a chord, it divides rest into two parts, which are independent of each other as intersection is not allowed.
we also divide them in even groups otherwise one will be left in both groups
"""
class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        # def findCnt(n):
        #     if dp[n]!=-1:
        #         return dp[n]
        #     cnt=0
        #     for i in range(n):
        #         cnt+=(findCnt(i)*findCnt(n-i-1))%10000000007
        #         cnt%=10000000007
        #     dp[n] = cnt
        #     return cnt
        dp=[-1]*(A+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,A+1):
            cnt=0
            for j in range(i):
                cnt+=(dp[j]*dp[i-j-1])%1000000007
                cnt%=1000000007
            dp[i] = cnt
        return dp[-1]%1000000007