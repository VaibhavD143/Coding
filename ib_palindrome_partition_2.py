class Solution:
    def minCut(self, A: str) -> int:
        if len(A)<2:
            return 0
        dp = list(range(1+len(A)))  #dp[i] : stores number of cuts required till ith index, inclusive
        dp[-1]=-1   #when it checks for dp[l-1] for l=0 it will get -1 as there is no count of partition before 0 ,so to componsate +1,-1.
        
        #just like longest palidromic substring, looking for each substring and updating required cuts accordingly
        for i in range(len(A)):
            dp[i]=min(dp[i-1]+1,dp[i])
            #Odd length
            l,r = i-1,i+1
            while l>=0 and r<len(A) and A[l]==A[r]:
                dp[r] = min(dp[r],1+dp[l-1])
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(A) and A[l]==A[r]:
                dp[r] = min(dp[r],1+dp[l-1])
                l-=1
                r+=1
        # print(dp)
        return dp[-2]   #as dp[-1] is dummy node to avoid overflow
        
        # def isPalin(s):
        #     return s == s[::-1]

        #here index ind is inclusive
        # def findMin(ind):
        #     if ind == len(A):
        #         return 0
        #     if dp[ind]!=-1:
        #         return dp[ind]
            #if string is already palindrome then no need of partition
        #     if isPalin(A[ind:]):
        #         dp[ind]=0
        #         return 0
        #     cnt = len(A)-ind-1    #maximum possible cut, if seperate each character
            #As whole A[ind:] is not palindrome, dividing it into A[ind:i] to A[i:]
        #     for i in range(len(A)-1,ind,-1):
        #         if isPalin(A[ind:i]): 
        #             cnt = min(cnt,1+findMin(i))
        #     dp[ind]=cnt
        #     return cnt
        # if not A:
        #     return 0
        # dp = [-1]*len(A)  #dp[i]: stores required cuts from ith index to end
        # dp[-1]=0  #no cuts on last single character
        # return findMin(0)