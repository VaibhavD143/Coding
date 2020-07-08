from collections import Counter
tc = int(input())
while tc:
    n,k = map(int,input().split())
    cnt = Counter(input())
    # keys = sorted(cnt,key=lambda i:cnt[i],reverse=True)
    divs = []
    for i in range(1,1+int(k**0.5)):
        if k%i ==0:
            divs.append(i)
            divs.append(k//i)
    # print(cnt)
    # print(keys)
    # print(divs)
    res = 0
    for i in divs:
        rep = 1
        while rep*i<=n:
            c = 0
            for k in cnt:
                c+=cnt[k]//rep
            if c>=i:
                res = max(res,rep*i)
            else:
                break
            rep+=1


    print(res)
    tc-=1