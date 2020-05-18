class Solution:
    def maxSubarraySumCircular(self, lst: List[int]) -> int:
        if not lst:
            return 0
        gsum =float('-inf')
        lsum = 0
        for x in lst:
            lsum = max(lsum+x,x)
            gsum=max(gsum,lsum)
        # print(gsum)
        gmin = float('inf')
        lmin = 0
        for x in lst:
            lmin=min(lmin+x,x)
            gmin=min(lmin,gmin)
        
        return max(gsum,sum(lst)-gmin) if gsum>0 else gsum #to handle case when all elements are -ve, then substraction would become 0 so gsum is answer