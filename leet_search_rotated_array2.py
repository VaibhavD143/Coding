"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Unsolved
"""
def search(nums, target):
        def binary_search(lst,elm):
            f = 0
            r = len(lst)
            pmid = -1
            mid = (f+r) //2

            while f != r:
                if lst[mid] == elm:
                    return mid
                elif lst[mid] > elm:
                    r = mid
                else:
                    f = mid+1

                pmid = mid
                mid = (f+r) //2
            # return mid #to return index of next present number
            return -1 #to return -1 if not present

        lst = nums
        n = len(lst)
        if n ==0:
            return False
        k = target
        i = 0
        j = n-1
        elem = lst[0]
        while i<j:
            mid = (i+j)//2
            print(i,mid,j)
            if lst[i]==lst[j]==lst[mid]:
                i+=1
                j-=1
            elif lst[mid]>elem:
                i=mid+1
            else:
                j=mid-1
        if lst[i] >= elem:
            part = (i+1)
        else:
            part = i
        print(part)
        return
        if k>=lst[0]:
            ind = binary_search(lst[:part],k)
        else:
            ind = binary_search(lst[part:],k)
            if ind !=-1:
                ind+=part
        return True if ind != -1 else False
print(search([1,3,1,1],3))