nums = [-1, 3, 1, -4,-1,2]
target = -4
nums.sort()
# cur_min = max(abs(nums[0]+nums[1]+nums[2]-target),abs(nums[-1]+nums[-2]+nums[-3]-target))
if abs(nums[0]+nums[1]+nums[2]-target) < abs(nums[-1]+nums[-2]+nums[-3]-target):
    cur_min = nums[0]+nums[1]+nums[2]
else:
    cur_min = nums[-1]+nums[-2]+nums[-3]
res = []
for i in range(len(nums)-1):
    if i>0 and nums[i-1] == nums[i]:
        continue

    low = i+1
    high = len(nums)-1

    while low<high :
        tot = nums[i]+nums[low]+nums[high]
        if tot<target:
            low+=1
        elif tot>target:
            high-=1
        else:
            cur_min = target
            print(cur_min,"final") #return from here
            break
        if abs(tot-target) < abs(cur_min-target):
            cur_min = tot
print(cur_min)