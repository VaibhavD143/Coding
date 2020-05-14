A =matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["1","1"],["1","1"]]
A =matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
def pr(mat):
    for r in mat:
        print(r)
pr(matrix)
if not len(matrix) or not len(matrix[0]):
    print(0)
    exit(1)
mat = [[0]*len(matrix[0]) for _ in range(len(matrix))]
mat[0][0] = res = 1 if matrix[0][0] == "1" else 0
for i in range(1,len(matrix[0])):
    if matrix[0][i] == "1":
        mat[0][i] = 1
        res = 1
for i in range(1,len(matrix)):
    if matrix[i][0] == "1":
        mat[i][0] = 1
        res = 1
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i][j] == "1":
            mat[i][j] = min(mat[i][j-1],mat[i-1][j],mat[i-1][j-1])+1
            res = max(res,mat[i][j])            
print(res*res)