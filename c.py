for tc in range(int(input())):
    n,a,b = map(int,input().split())
    lst = list(map(int,input().split()))
    ha = [[] for _ in range(n+1)]
    ha[1].append(1)
    res = 0
    for i in range(2,1+n):
        k = i
        # path = []
        while True:
            if ha[k]:
                ha[i].extend(ha[k])
                break
            ha[i].append(k)
            k = lst[k-2]
    for i in range(1,n+1):
        path = set(ha[i][::a])
        for j in range(1,n+1):
            tpath = path|set(ha[j][::b])
            res+=len(tpath)
    print("Case #{}: {}".format(tc+1,res/(n**2)))