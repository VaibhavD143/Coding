class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        res=0
        for i in range(len(matrix)):
            res+=matrix[i][0]
        for j in range(1,len(matrix[0])):
            res+=matrix[0][j]
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                    res+=matrix[i][j]
                
#         for r in matrix:
#             print(r)
        return res