from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    # p = [None]*n
    # h = [None]*n
    lst = [None]*n
    for i in range(n):
        lst[i] = list(map(int,input().split()))
    lst.sort()
    ha=defaultdict(int)
    res = 0
    for d,l in lst:
        ha[d+l] = max(ha[d+l],ha[d]+l)
        ha[d] = max(ha[d],ha[d-l]+l)
        res = max(res,ha[d],ha[d+l])
    print(F'Case #{_+1}: {res}')