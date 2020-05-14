lst = [4,1,5,2,3,6]
# lst = [2,1,3,4]
lst = [15,5,15]
part = 2
# part-=1
pref = [0]*(len(lst)+1)
for i in range(1,1+len(lst)):
    pref[i] = pref[i-1]+lst[i-1]

dp =[[None]*len(lst) for _ in range(part)]

for i in range(len(lst)):
    dp[0][i] = pref[i+1]**2

for i in range(1,part):
    for j in range(i,len(lst)-(part-i-1)):
        minVal = float('inf')
        for k in range(i-1,j):
            minVal = min(minVal,dp[i-1][k]+(pref[j+1]-pref[k+1])**2)
        dp[i][j]= minVal
for r in dp:
    print(r)

print(dp[-1][-1])