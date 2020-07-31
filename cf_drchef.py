from collections import defaultdict
from bisect import bisect_left

for _ in range(int(input())):
    n,x = map(int,input().split())
    lst = sorted(map(int,input().split()))
    # ha = defaultdict(int)
    # mx = 1
    # for n in lst:
    #     ha[n]+=1
    #     mx = max(mx,n)
    if x>=lst[-1]:
        print(len(lst))
        continue
    mx = rem = lst.pop()
    res = 0
    while x<=rem:
        ind = bisect_left(lst,x)
        if ind <len(lst) and lst[ind] == x:
            lst[ind] = 0
        res+=1
        rem-=x
        x*=2
    print(lst,res)
    while lst and rem<lst[-1]:
        x = 2*lst.pop()
        res+=1
        rem =min(2*rem,mx)
    res+=1 #for rem
    for n in lst:
        if n:
            res+=1
    print(res)