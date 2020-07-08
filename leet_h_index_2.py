class Solution:
    def hIndex(self, ci: List[int]) -> int:
        if not ci or ci[-1]==0:
            return 0
        lo,hi=0,len(ci)-1
        while lo<hi:
            mid = lo+(hi-lo)//2
            if ci[mid]>=len(ci)-mid:
                hi=mid
            else:
                lo=mid+1
        return len(ci)-lo