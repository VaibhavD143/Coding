class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        res = [1]*B #keeping it 1 to handle case B=1
        high = B
        low = 1
        for i in range(len(A)):
            if A[i]=='I':
                res[i] = low
                low+=1
            else:
                res[i] = high
                high-=1
        res[-1] =low
        return res
            