"""Intution:
dp[i] = stores length of valid parentheses ending on ith index
if ith index is '(' => 0
                ')' => skip valid string length stored in dp[i-1] if match then add that string(i-ind+1)+string before that (if any,dp[ind-1])
$ to avoid out of index check"""

class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        s = '$'+A
        dp = [0]*len(s)
        
        for i in range(1,len(dp)):
            if s[i] == '(':
                dp[i]=0
            else:
                diff = dp[i-1]
                ind = i-diff-1
                if s[ind] == '(':
                    dp[i] = (i-ind+1)+dp[ind-1]
                else:
                    dp[i]=0
        return max(dp)