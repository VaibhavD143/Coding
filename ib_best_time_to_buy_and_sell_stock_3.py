class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<2:
            return 0
        left = [0]*(1+len(A))
        right = [0]*(1+len(A))
        currMin = A[0]
        for i in range(1,len(A)):
            left[i+1] = max(A[i]-currMin,left[i])
            currMin = min(currMin,A[i])
        currMax = A[-1]
        for i in range(len(A)-2,-1,-1):
            right[i] = max(currMax-A[i],right[i+1])
            currMax = max(currMax,A[i])
        # print(left)
        # print(right)
        res=0
        for i in range(len(A)):
            res = max(res,left[i]+right[i])
        return res