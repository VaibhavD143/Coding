"""
Intution:
1)
TLE:
check for each possible configuration of color tuple and if it is allowed then add to the result
2)
THere are two types of combinations:
1- (x,y,z) col3 : one col3 tuple generates new 11 col3 combinations, 5 col2 combination
2- (x,y,x) col2 : one col2 tuple generates new 10 col3 combinations, 7 col2 combination
take an example and follow for related questions

https://www.geeksforgeeks.org/ways-color-3n-board-using-4-colors/
"""
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        colors = [1,2,3,4]
        possible =[]
        for i in colors:
            for j in colors:
                for k in colors:
                    if i!=j and j!=k:
                        possible.append((i,j,k))

        #Three clors possibilities(x,y,z)
        col3 = 24
        #Two color combinations(x,y,x)
        col2 = 12
        tmp = 0
        mod = 10**9+7
        for i in range(1,A):
            tmp=col3
            col3 = ((11*col3)%mod+(10*col2)%mod)%mod
            col2 = ((5*tmp)%mod+(7*col2)%mod)%mod
        return (col2+col3)%mod


        # dp=[[0]*(A) for _ in range(36)]
        # for i in range(36):
        #     dp[i][0]=1
        # for i in range(1,A):
        #     for ind1,curr in enumerate(possible):
        #         for ind2,prev in enumerate(possible):
        #             if curr[0]!= prev[0] and curr[1]!=prev[1] and curr[2]!=prev[2]:
        #                 dp[ind1][i]+=dp[ind2][i-1]
        #                 dp[ind1][i]%=1000000007
        # for ind,r in enumerate(dp):
        #     print(possible[ind],r)
        # ans = 0
        # for i in range(36):
        #     ans += dp[i][-1]
        #     ans %= 1000000007
        # return ans