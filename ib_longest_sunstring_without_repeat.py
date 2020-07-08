from collections import defaultdict
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        l,r=0,0
        ha = defaultdict(int)
        res = 0
        while r<len(A):
            ha[A[r]]+=1
            if ha[A[r]]>1:
                while ha[A[r]] > 1:
                    ha[A[l]]-=1
                    l+=1
            res = max(res,r-l+1)
            r+=1
        return res