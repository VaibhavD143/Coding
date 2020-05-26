import bisect
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        # return bisect.bisect_left(A,B)
        if B<=A[0]:
            return 0
        if B>A[-1]:
            return len(A)
        low=0
        high = len(A)-1
        # ind=len(A)
        # while low<=high:
        while low<high:
            mid = low+(high-low)//2
            if A[mid]==B:
                return mid
            
            if A[mid]<B:
                low=mid+1
            else:
                # ind=mid
                high=mid
        return low #ind