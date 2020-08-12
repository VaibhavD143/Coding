from collections import Counter
#code
for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = Counter(map(int,input().split()))
    mx = max(lst)
    c = lst[mx]
    res = 0
    while k>0:
        res+=min(c,k)*mx
        k-=c
        mx-=1
        if mx in lst:
            c+=lst[mx]
    print(res)