"""
https://leetcode.com/problems/house-robber/
"""
nums = [2]
if len(nums) == 1:
    print(nums[0])
dp = [0]*len(nums)
dp[0] = nums[0]
dp[1] = max(nums[0],nums[1])

for i in range(2,len(nums)):
    dp[i] = max(nums[i]+dp[i-2],dp[i-1])
print(dp[-1])