for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    res = 0
    for i in range(1,len(lst)):
        if lst[i]!=lst[i-1]:
            res+=abs(lst[i]-lst[i-1])-1
    print(res)
