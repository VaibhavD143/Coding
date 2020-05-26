class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, lst):
        l=0
        r=len(lst)-1
        i=0
        while i<=r:
            if lst[i]==0:
                lst[i],lst[l]=lst[l],lst[i]
                i+=1
                l+=1
            elif lst[i]==1:
                i+=1
            else:
                lst[r],lst[i]=lst[i],lst[r]
                r-=1
            
        return lst