for tc in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    sm = nsm = 0
    max_sm = lst[0]
    min_sm = lst[0]
    for n in lst:
        sm+=n
        nsm+=n
        max_sm = max(sm,max_sm)
        min_sm = min(nsm,min_sm)
        if sm<0:
            sm=0
        if nsm>0:
            nsm=0
    
    if max_sm<0:
        print("Case #{}: {}".format(tc+1,0))
        continue
    
    sq = [i*i for i in range(int(max_sm**0.5)+1)]
    cnt= [0]*len(sq)
    
    sm =0
    # ha = {sm:1}
    offset = min(0,min_sm)*-1
    ha = [0]*(max_sm+1+offset)
    ha[offset] = 1
    for n in lst:
        sm+=n
        for i,s in enumerate(sq):
            diff = sm-s+offset
            cnt[i]+=ha[diff]
            if diff<=0:
                break
        ha[sm+offset]+=1
    # print(min_sm,max_sm)
    # print(sq)
    # print(cnt)
    # print(ha)
    print("Case #{}: {}".format(tc+1,sum(cnt)))