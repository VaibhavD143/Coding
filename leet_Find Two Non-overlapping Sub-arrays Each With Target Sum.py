"""
Intution:
we are storing best possible subarray length in right[i] and summing up
"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ha= {0:-1}
        first = [float('inf')]*(len(arr)+1)
        curr = 0
        res = float('inf')
        for i,n in enumerate(arr):
            curr+=n
            if curr-target in ha:
                ind = ha[curr-target]
                first[i+1] = min(i-ind,first[i])
                res = min(res,first[ind+1]+(i-ind))
            else:
                first[i+1] = first[i]
            ha[curr] = i
        return res if res!=float('inf') else -1
        
                
        # right=[float('inf')]*len(arr)
        # l,r=0,0
        # cur = 0
        # for r in range(len(arr)):
        #     cur+=arr[r]
        #     if cur == target:
        #         right[r] = r-l+1
        #         cur-=arr[l]
        #         l+=1
        #     elif cur>target:
        #         while cur>target:
        #             cur-=arr[l]
        #             l+=1
        #         if cur==target:
        #             right[r] = r-l+1
        #             cur-=arr[l]
        #             l+=1
            # r+=1
        # # print(right)
        # left=[float('inf')]*len(arr)
        # curMin = float('inf')
        # for i in range(len(arr)-1,-1,-1):
        #     if right[i]!=float('inf'):
        #         left[i-right[i]+1] = min(right[i],left[i+1] if i!=len(arr)-1 else float('inf'))
        #     if i!=len(arr)-1:
        #         left[i]=min(left[i],left[i+1])
        # res=float('inf')
        # for i in range(1,len(right)):
        #     if i-right[i]>=0 and right[i]!=float('inf') and right[i-right[i]]!=float('inf'):
        #         res = min(res,right[i]+right[i-right[i]])
        #     right[i]=min(right[i],right[i-1])
        # # for i in range(len(arr)-1):
        # #     res = min(res,right[i]+left[i+1])
        # return res if res!=float('inf') else -1
