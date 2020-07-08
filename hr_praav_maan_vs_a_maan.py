def update(val,ind):
    ind +=1
    while ind<len(bit):
        if bit[ind]>val:
            break
        bit[ind] = val
        ind += (ind&-ind)
    
def getMax(ind):
    ind+=1
    res = 0
    while ind>0:
        res = max(res,bit[ind])
        ind-=(ind&-ind)
    return res

n = int(input())
lst = list(map(int,input().split()))
n=5
lst = [9,2,8,5,6]
bit = [float('-inf')]*(n+1)
loc = [[val,i] for i,val in enumerate(lst)]
loc.sort()
dp = [0]*len(lst)
res = float('-inf')
for i in range(len(lst)):
    ind = loc[i][1]
    dp[ind] = loc[i][0]
    m = getMax(ind)
    if m+lst[ind]>dp[ind]:
        dp[ind] = m+lst[ind]
    update(dp[ind],ind)
    res = max(res,dp[ind])
print(res)



