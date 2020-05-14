class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, mat):
        if not len(mat) or not len(mat[0]):
            return
        rowSum=[]
        for r in mat:
            rowSum.append(sum(r))
        colSum=[]
        for i in range(len(mat[0])):
            colSum.append(sum(map(lambda item:item[i],mat)))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rowSum[i]<len(mat[0]) or colSum[j]<len(mat):
                    mat[i][j]=0
                