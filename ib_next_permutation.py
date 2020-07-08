class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        i=len(A)-2
        while i>=0:
            if A[i]<A[i+1]:
                break
            i-=1
        if i ==-1:
            return A[::-1]
        for j in range(len(A)-1,i-1,-1):
            if A[j]>A[i]:
                A[i],A[j] = A[j],A[i]
                break
        A[i+1:]=A[i+1:][::-1]
        return A