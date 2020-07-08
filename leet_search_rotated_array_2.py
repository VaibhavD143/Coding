class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l,r=0,len(nums)-1
        while l<=r:
            mid =l+(r-l)//2
            # print(mid)
            if nums[mid] == target:
                return True
            
            if nums[l]<nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[l]>nums[mid]:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                i = mid
                while l<i and nums[i]==nums[mid]:
                    i-=1
                #left part is sorted
                if l==i:
                    if target>nums[mid] or target<nums[l]:
                        l=mid+1
                    #because left part has only elements nums[mid] which is not a answer
                    else:
                        return False
                #right part is sorted
                else:
                    if target<nums[mid] or target>nums[r]:
                        r=mid-1
                    #because array is divided into two part for sure as left part is not sorted
                    #as nums[l] and nums[mid] are same, all elements in right part will be same as nums[mid], which is not an answer
                    else:
                        return False
                    
        return False