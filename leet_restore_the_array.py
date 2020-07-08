class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        l=len(str(k))
        dp = [0]*(len(s)+l) #+l to avoid messy condition checks for last l elements
        dp[-l]=1    #when we select string till last element

        for i in range(len(s)-1,-1,-1):

            #no number starting from 0 is allowed, so skip it
            if s[i]=='0':
                continue

            #number starting from index i and having length from 1 to l-1,a s they all are valid
            for j in range(i,i+l-1):
                dp[i]+=dp[j+1]

            #if length is same then check for validity
            if i+l-1<len(s) and int(s[i:i+l])<=k:
                dp[i]+=dp[i+l]

            dp[i]%=1000000007
        return dp[0]