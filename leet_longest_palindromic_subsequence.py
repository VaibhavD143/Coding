s = "bababbd"
s = "cbbd"
s = "ababba"
s = "abccbba"
rs = s[::-1]

dp = [[-1]*len(s) for _ in range(len(s))]

def fun(s,rs,ins,inrs,dp):
    if ins >= len(s) or inrs >= len(rs):
        return 0
    if dp[ins][inrs] != -1:
        return dp[ins][inrs]
    if s[ins] == rs[inrs]:
        dp[ins][inrs] = max(1+fun(s,rs,ins+1,inrs+1,dp),fun(s,rs,ins+1,inrs,dp),fun(s,rs,ins,inrs+1,dp))
    else:
        dp[ins][inrs] = max(fun(s,rs,ins+1,inrs,dp),fun(s,rs,ins,inrs+1,dp))
    return dp[ins][inrs]

print(fun(s,rs,0,0,dp))
print(" ",*rs)
i=0
for rw in dp:
    print(s[i],*rw)
    i+=1