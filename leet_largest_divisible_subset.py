class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [0]*len(nums)
        parent = [-1]*len(nums)
        res = 0
        start = None
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i] ==0 and dp[j]>dp[i]:
                    dp[i] = dp[j]
                    parent[i] = j
            dp[i]+=1    #adding itself
            if res<dp[i]:
                start = i
                res = dp[i]
        res = []
        while parent[start]!=-1:
            res.append(nums[start])
            start = parent[start]
        res.append(nums[start])
        return res