"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
def canPartition(nums) -> bool:
        sum_nums = sum(nums)
        if sum_nums&1:
            return 0
        k = sum_nums//2
        dp = [0]*(k+1)
        dp[0]=1
        for num in nums:
            for j in range(k-num,-1,-1):
                if dp[j]:
                    dp[j+num]=1
            if dp[-1]:
                return 1
        return 0

