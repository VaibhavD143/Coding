for _ in range(int(input())):
    n = int(input())
    mat = [['N']*n for _ in range(n)]
    for i in range(n):
        mat[i][i] = 'Y'
    inc = input()
    out = input()
    lst =[]
    for i in range(n):
        if inc[i]=='Y':
            for u in lst:
                mat[u][i] = 'Y'
        else:
            lst=[]
        if out[i] == 'Y':
            lst.append(i)
        else:
            lst = []
    lst = []
    for i in range(n-1,-1,-1):
        if inc[i] == 'Y':
            for u in lst:
                mat[u][i] = 'Y'
        else:
            lst = []
        if out[i] == 'Y':
            lst.append(i)
        else:
            lst=[]
    print(F'Case #{_+1}:')
    for r in mat:
        print(''.join(r))
    
