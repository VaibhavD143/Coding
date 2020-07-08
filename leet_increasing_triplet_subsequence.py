"""
Intution:
a,b are current memeber of sequence
a1 is next potetial candidate

"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        # a,b,a2=nums[0],None,None
        # for n in nums[1:]:
        #     if a<n:
        #         #when only one element in current sequence, add second
        #         if b==None:
        #             b = n
        #         #two elements and this is third element, so true
        #         elif b<n:
        #             return True
        #         #if greater than first but lesser than second, then change second i.e [a,b,n...] [2,6,3...]
        #         elif b>n:
        #             b= n
        #     elif a>=n:
        #         #if only one element,and lesser than first element i.e. [a,n.....] [3,2.....]
        #         if b == None:
        #             a=n
        #         #two elements and if lesser than first, then for sure lesser than second as `a<b`
        #         #if candidate is not assigned then assign i.e. [a,b,n] [3,5,2]
        #         elif a2 == None:
        #             a2= n
        #         #if candidate is assigned but lower than candidate i.e. [a,b,a2,n] [3,6,2,1]
        #         elif a2>n:
        #             a2=n
        #         #if n is greater than cadidate and as we have established, n<a<b and so we change current sequence to potential sequence
        #         #i.e. [a,b,a1,n] [4,6,3,4,...5]
        #         elif a2<n:
        #             a=a2
        #             b=n
        #             a2=None
        # return False
        small,big = float('inf'),float('inf')
        for n in nums:
            if small>=n:
                small = n
            elif big>=n:
                big = n
            else:
                return True
        return False