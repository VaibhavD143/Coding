class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        for i in range(1,len(A)):
            A[i][0]+=A[i-1][0]
            A[i][-1]+=A[i-1][-1]
        
        for i in range(1,len(A)):
            for j in range(1,len(A[i])-1):
                A[i][j]=A[i][j]+min(A[i-1][j-1],A[i-1][j])
        return min(A[-1])