class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<2:
            return 0
        curr=A[-1]
        res=0
        for i in reversed(A):
            curr = max(curr,i)
            res = max(res,curr-i)
        return res