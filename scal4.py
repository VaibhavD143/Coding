lst = [4,1,5,2,3,6]
# lst = [2,1,3,4]
# lst = [15,5,15]
part = 3

def partMe(dp,lst,ind,part,pref):
    print(part,ind)
    if dp[part][ind] != None:
        return dp[part][ind]
    if part ==0:
        dp[part][ind] = (pref[-1]-pref[ind])**2
        return dp[part][ind]
    curr_ans = float('inf')
    for i in range(ind+1,len(lst)-part+1):
        curr_ans = min(curr_ans,partMe(dp,lst,i,part-1,pref)+(pref[i]-pref[ind])**2)
    dp[part][ind] = curr_ans
    return dp[part][ind]
    
pref = [0]*(len(lst)+1)
for i in range(1,1+len(lst)):
    pref[i] = pref[i-1]+lst[i-1]

dp =[[None]*len(lst) for _ in range(part)]

res = float('inf')
# if part == 1:
#     return pref[-1]**2
part-=1
for i in range(1,len(lst)-part+1):
    print(partMe(dp,lst,i,part-1,pref),(pref[i])**2,partMe(dp,lst,i,part-1,pref)+(pref[i])**2,res)
    res = min(res,partMe(dp,lst,i,part-1,pref)+(pref[i])**2)
print(res)