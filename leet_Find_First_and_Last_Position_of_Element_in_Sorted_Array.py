def binary_search(lst,elm):
    f = 0
    r = len(lst)
    pmid = -1
    mid = (f+r) //2

    while f != r:

        print('in',f,mid,r)
        if lst[mid] == elm:
            r = mid
            # return mid
        elif lst[mid] > elm:
            r = mid
        else:
            f = mid+1

        pmid = mid
        mid = (f+r) //2
    return mid #to return index of next present number
    # return -1 #to return -1 if not present

nums = [5,7,7,9,9,10]
target = 11
nums = [7]
target = 7
start = binary_search(nums,target)
print(start)
end = binary_search(nums,target+1)
print(end)
if start == end or start>len(nums) or nums[start] !=target:
    ans = [-1,-1]
elif nums[start] == target:
    ans = [start,end-1]
print(ans)