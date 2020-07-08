lst = [1,2,3]

res = [[]]
for i in range(len(lst)):
    for j in range(len(res)):
        res.append(res[j]+[lst[i]])
print(res)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def rec(ind):
            if ind == len(nums):
                # res.append(lst[:])
                return
            lst.append(nums[ind])
            res.append(lst[:])
            rec(ind+1)
            lst.pop()
            rec(ind+1)
        res = []
        lst = []
        rec(0)
        return [[]]+res