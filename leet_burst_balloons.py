
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def rec(start,end):
            # if start == end:
            #     return 0
                # return nums[start]
            if end-start == 1:
                return 0
                # return nums[start]*nums[end]+max(nums[start],nums[end])
#             if end-start == 2:
#                 return nums[start]*nums[start+1]*nums[end]+nums[start]*nums[end]+max(nums[start],nums[end])
            
            if (start,end) in ha:
                return ha[start,end]
            
            res = float('-inf')
            for k in range(start+1,end):
                tres = rec(start,k)+rec(k,end)+nums[start]*nums[k]*nums[end]
                res = max(res,tres)
            ha[start,end] = res
            return res
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        nums = [1]+nums+[1]
        ha={}
        return rec(0,len(nums)-1)