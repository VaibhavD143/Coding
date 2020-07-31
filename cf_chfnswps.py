from collections import Counter

for _ in range(int(input())):
    n = int(input())
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))
    cnt1 = Counter(lst1)
    cnt2 = Counter(lst2)
    tot = cnt1+cnt2
    elems = sorted(tot.keys(),reverse=True)
    d1 = []
    d2 = []
    flag = 0
    min_elem = elems[-1]
    # print(cnt1,cnt2,tot )
    for e in elems:
        if tot[e]&1:
            print(-1)
            flag = 1
            break
        half= tot[e]//2
        
        if  half < cnt1[e]:
            d1.extend([e]*(cnt1[e]-half))
        elif half<cnt2[e]:
            d2.extend([e]*(cnt2[e]-half))
    # print(d1,d2)
    if not flag:
        diff= len(d1)
        res=0
        while diff:
            mn = min(d1[-1],d2[-1])
            if mn>=2*min_elem:
                break
            res+=mn
            if mn == d1[-1]:
                d1.pop()
            else:
                d2.pop()
            diff-=1
        res+=(2*min_elem*diff)
        print(res)