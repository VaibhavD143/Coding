for _ in range(int(input())):
    n = int(input())
    res = [['.']*8 for _ in range(8)]
    res[0][0] = 'O'
    r,c=divmod(n-1,8)
    for i in range(c+1,8):
        res[r][i] = 'X'
    if r<7:
        for j in range(min(c+2,8)):
            res[r+1][j] = 'X'
    for r in res:
        print(''.join(r))