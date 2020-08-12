for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    res = [1]*n
    for i in range(1,n):
        if lst[i-1]<lst[i]:
            res[i]=res[i-1]+1
    sm = 0
    for i in range(n-2,-1,-1):
        if lst[i]>lst[i+1] and res[i]<=res[i+1]:
            res[i] = res[i+1]+1
        sm+=res[i]
    # print(res)
    print(sm+res[-1])