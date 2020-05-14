"""
https://leetcode.com/problems/3sum/
triplates with sum 0
with repeatation of number
"""

nums = [-1, 0, 1,-1, 2, -4]
nums = [0,0,0]
nums = [-2,0,0,2,2]
l_nums = len(nums)

nums.sort()
res = []
for i in range(l_nums-1):
    if i>0 and nums[i-1] == nums[i]:
        continue

    low = i+1
    high = l_nums-1

    while low<high :
        tot = nums[i]+nums[low]+nums[high]
        if tot<0:
            low+=1
        elif tot>0:
            high-=1
        else:
            res.append([nums[i],nums[low],nums[high]])
            while low<high and nums[low] == nums[low+1]:
                low+=1
            while low<high and nums[high] == nums[high-1]:
                high-=1
            low+=1
            high-=1
print(res)