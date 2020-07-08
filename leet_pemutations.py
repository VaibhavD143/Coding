class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(ind):
            if ind == len(nums):
                res.append(lst[:])
            
            for i in range(ind,len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind]
                lst.append(nums[ind])
                rec(ind+1)
                lst.pop()
                nums[ind],nums[i] = nums[i],nums[ind]
        
        res = []
        lst = []
        rec(0)
        return res