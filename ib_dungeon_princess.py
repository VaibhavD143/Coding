"""
Intution:
It won't work from top-left like other problems, as here negative is also possible
In return we are making it 0 and not positive as , positive effect is from that to end and we are moving backwards
"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        A[-1][-1]=min(A[-1][-1],0)
        for i in range(len(A)-2,-1,-1):
            A[i][-1]=min(A[i+1][-1]+A[i][-1],0)
        for j in range(len(A[0])-2,-1,-1):
            A[-1][j] = min(A[-1][j+1]+A[-1][j],0)
            
        for i in range(len(A)-2,-1,-1):
            for j in range(len(A[0])-2,-1,-1):
                A[i][j] = max(min(A[i+1][j]+A[i][j],0),min(A[i][j+1]+A[i][j],0))
        return (-1*A[0][0])+1