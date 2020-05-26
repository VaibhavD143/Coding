class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        l=1
        r=len(A)-2
        #Find first occurence from both side when array is not sorted
        while l<len(A) and A[l]>=A[l-1]:
            l+=1
        if l==len(A):
            return [-1]
        while r>=0 and A[r]<=A[r+1]:
            r-=1
        
        #Find max and min it has in unsorted list i.e. 1 2 9 4 11 6 5 7 10 15
        lmax=A[l-1]
        rmin=A[r+1]
        tl=l
        while tl<=r:
            lmax=max(lmax,A[tl])
            rmin=min(rmin,A[tl])
            tl+=1
        #Get those indexes
        l,r=0,len(A)-1
        while A[l]<=rmin:
            l+=1
        while A[r]>=lmax:
            r-=1
        return [l,r]
        