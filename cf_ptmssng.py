for _ in range(int(input())):
    row = {}
    col = {}
    for _ in range(int(input())*4-1):
        r,c = map(int,input().split())
        row[r] = row.get(r,0)+1
        col[c] = col.get(c,0)+1
    for k,val in row.items():
        if val&1:
            r = k
            break
    for k,val in col.items():
        if val&1:
            c = k
            break
    print(r,c)