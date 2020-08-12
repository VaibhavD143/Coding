from collections import Counter

low = "0"
hi = "5"

if len(low)!=len(hi):
    low = '0'*(len(hi)-len(low))+low


def rec(ind,sm,bound,lim):
    if ind == len(lim):
        return Counter([sm])
    
    if (ind,sm,bound) in dp:
        return dp[ind,sm,bound]
    
    cnt = Counter()
    for i in range(10):
        if bound and str(i) == lim[ind]:
            cnt+=rec(ind+1,sm+i,True,lim)
            break
        cnt+=rec(ind+1,sm+i,False,lim)
    dp[ind,sm,bound] = cnt
    return cnt 

dp = {}
cnt1 = rec(0,0,True,hi)
dp={}
cnt2 = rec(0,0,True,low)
cnt = cnt1-cnt2
mx = max(cnt.values())
c = 0
for i,v in cnt.items():
    if v == mx:
        c+=1
print(c,mx)