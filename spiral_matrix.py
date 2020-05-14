9909082621
#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

mat = [[ 1, 2, 3,10 ],[ 4, 5, 6,11 ],[ 7, 8, 9,12 ]]
# mat = []
# lc = 0
# rc =cols-1
# tr = 0
# br = rows-1

# while rows>0 or cols>0:
#     for i in range(cols-1):
#         print(mat[tr][i],end=" ")
#     for i in range(rows-1):
#         print(mat[i][rc],end=" ")
#     for i in range(cols-1,0,-1):
#         print(mat[br][i],end=" ")
#     for i in range(rows-1,0,-1):
#         print(mat[i][lc],end=" ")
#     lc +=1
#     rc -=1
#     tr +=1
#     br -=1
#     rows-=2
#     cols-=2
def fun(mat,rows,cols):
    while mat:
        yield mat.pop(0)
        rows-=1
        for i in range(rows-1):
            yield [mat[i].pop()]
        if rows>0:
            yield reversed(mat.pop())
        rows-=1
        for i in range(rows-1,-1,-1):
            yield [mat[i].pop(0)]
def fun2(matrix):
    ans = []
    rows = len(matrix)
    if rows:
        cols = len(matrix[0])
    while matrix:
        ans.extend(matrix.pop(0))
        rows-=1
        for i in range(rows-1):
            ans.append(matrix[i].pop())
        if rows>0:
            ans.extend(reversed(matrix.pop()))
            rows-=1
        for i in range(rows-1,-1,-1):
            ans.append(matrix[i].pop(0))
    return ans
# mat = [[]]
print(fun2(mat))