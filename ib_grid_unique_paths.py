class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        # dp= [1]*A
        # for i in range(1,B):
        #     r= dp[:]
        #     for j in range(1,A):
        #         r[j]=dp[j]+r[j-1]
        #     dp=r
        # return dp[-1]
        
        n = A+B-2
        r = A-1
        fact = [1]
        for i in range(1,n+1):
            fact.append(fact[-1]*i)
        return fact[n]//(fact[r]*fact[n-r])
        