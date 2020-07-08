class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # for i in range(1,len(nums)):
        #     if nums[i-1]>nums[i]:
        #         return i-1
        # return len(nums)-1
        lo,hi = 0,len(nums)-1
        while lo<hi:
            mid = lo+(hi-lo)//2
            if nums[mid]>nums[mid+1]:
                hi=mid
            else:
                lo=mid+1
        return lo