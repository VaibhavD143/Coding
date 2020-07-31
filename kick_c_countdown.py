for tc in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    tk = k
    i=0
    cnt=0
    for i in range(n):
        if lst[i] == tk:
            tk-=1
            if tk==0:
                cnt+=1
                tk=k
        elif lst[i] == k:
            tk=k-1
            if tk==0:
                cnt+=1
                tk=k
        else:
            tk=k
    print("Case #{}: {}".format(tc+1,cnt))