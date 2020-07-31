"""
Intution:
Find group for each element and do exhaustive search!
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target,rem = divmod(sum(nums),k)
        if rem:
            return False
        
        def rec(group):
            nonlocal target
            if not nums:
                # print(group)
                return all(target==group[i] for i in range(len(group)))
            n = nums.pop()
            for i in range(len(group)):
                group[i]+=n
                if group[i]<=target and rec(group):
                    return True
                group[i]-=n
                #Best possible condition!!
                #if adding this number to ith empty group couldn't help then it won't help in next empty buckets
                #upcoming buckets will be empty as we try to fill prev buckets first
                if group[i] == 0:
                    break
            nums.append(n)
            return False
        
        nums.sort()
        if nums[-1]>target:
            return False
        while nums[-1]==target:
            nums.pop()
            k-=1
        group = [0]*k
        res = rec(group)
        # print(group,target,sum(nums))
        return res