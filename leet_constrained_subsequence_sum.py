"""
Intution:
at any time we are interested in last k sums,
so we maintain a queue of those calculates values
here nums[i] stores maximum sum possible in sequence till ith index including ith element
"""
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        wind = deque([0])
        for i in range(1,len(nums)):
            while wind and wind[0]<i-k:
                wind.popleft()
            nums[i] = max(nums[i],nums[i]+nums[wind[0]])
            
            while wind and nums[wind[-1]]<nums[i]:
                wind.pop()
        
            wind.append(i)
        
        return max(nums)
                