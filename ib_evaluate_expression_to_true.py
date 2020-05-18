"""
dp[i][j] = expression from ith to jth operand
dp[i][j][0] = how many time it can be FALSE
dp[i][j][1] = how many time it can be TRUE
"""
class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        
        def giveCount(left,right,operator):
            ans=[0,0]
            if operator == '|':
                ans[1]=left[1]*right[1]+left[1]*right[0]+left[0]*right[1]
                ans[0]=left[0]*right[0]
            elif operator == '&':
                ans[1] = left[1]*right[1]
                ans[0] = left[0]*right[0]+left[0]*right[1]+left[1]*right[0]
            elif operator == '^':
                ans[1] = left[0]*right[1]+left[1]*right[0]
                ans[0] = left[0]*right[0]+left[1]*right[1]
            return ans
        A = A.replace("T",'1').replace("F",'0')
        A = [val if i&1 else int(val) for i,val in enumerate(A)]
        # print(A)
        n = (len(A)+1)//2
        dp = [[[0]*2 for _ in range(n)]for _ in range(n)]
        #filling up values as per the operand, will be working with upper triangle only
        for i in range(n):
            dp[i][i]=[1-A[i*2],A[i*2]]

        for k in range(1,n):
            i = 0
            for j in range(k,n):
                # print('---------')
                # print(i,j)
                res = [0,0]
                for r in range(i,j):
                    # print(i,r,A[1+2*r],r+1,j)
                    tmp = giveCount(dp[i][r],dp[r+1][j],A[1+2*r])
                    res[0]+=tmp[0]
                    res[1]+=tmp[1]
                dp[i][j][0]=res[0]
                dp[i][j][1]=res[1]
                # for r in dp:        
                #     print(r)
                i+=1
        return dp[0][-1][1]%1003