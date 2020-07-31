#code
for _ in range(int(input())):
    n = int(input())
    lad = {}
    sna = {}
    lst = list(map(int,input().split()))
    for l,r in zip(lst[::2],lst[1::2]):
        if r>l:
            lad[l] = r
        else:
            sna[l] = r
    # print(lad,sna)
    path = list(range(31))
    path[1]=0
    i=1
    while i<31:
        # print(path)
        if i not in sna and i not in lad:
            for j in range(i+1,min(31,i+7)):
                path[j] = min(path[j],path[i]+1)
        if i in lad:
            path[lad[i]] = min(path[lad[i]],path[i])
        i+=1
    # print(path)
    print(path[-1])