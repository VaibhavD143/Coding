"""
Intution:

"""
class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A or A[0]=='0':
            return 0
        dp = [0]*(len(A)+1)
        dp[0] = 1
        #ex : 0
        dp[1] = 1 if A[0] != '0' else 0
        
        for i in range(2,len(A)+1):
            dp[i] = dp[i-1] if A[i-1]!= '0' else 0
            #102 while processing on index 2
            if 9<int(A[i-2:i]) <= 26:
                dp[i]+=dp[i-2]
        return dp[-1]