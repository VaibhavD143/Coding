class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        if m*k>len(bloom):
            return -1
        low,high = 1,max(bloom)
        while low<high:
            mid = low+(high-low)//2
            bs = 0      # bouquets
            fs = 0    #flowers
            for d in bloom:
                if d<=mid:
                    fs+=1
                else:
                    fs=0
                if fs==k:
                    bs+=1
                    fs=0
                    if bs==m:
                        break
            if bs==m:
                high=mid
            else:
                low=mid+1
        return low
                