class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        l,r=0,1
        B = abs(B)
        while r<len(A):
            if A[r]-A[l] == B:
                return 1
            if A[r]-A[l] > B:
                l+=1
                if l==r:
                    r+=1
            else:
                r+=1
        return 0