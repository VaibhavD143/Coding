def driver(nums):
    if len(nums) <= 1:
        return
    flag= 0
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            flag = 1
            break
    if flag==0:
        nums[:]=nums[::-1]
    else:
        nums[i+1:]=nums[i+1:][::-1]
        print("in1",nums)
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
                break
    

nums = [1,3,5,4,2]
nums = [4,5,4,3,2,1]
print(nums)
driver(nums)
print(nums)