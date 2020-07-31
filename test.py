mat= [[]]
for i in range(1,len(mat)):
    for j in range(len(mat[0])):
        mat[i][j] +=mat[i-1][j]

res = float('-inf')
for r1 in range(len(mat)):
    for r2 in range(r1,len(mat)):
        sm = 0
        for j in range(len(mat[0])):
            sm+= mat[r2][j] - (mat[r1-1][j] if r1!=0 else 0)
            res = max(res,sm)
            if sm<0:
                sm = 0
return res