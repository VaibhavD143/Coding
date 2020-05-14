#2,6,7
d,f,target = 1,6,3
d,f,target = 1,6,3
d,f,target = 2,5,10
# d,f,target = 1,2,3
# d,f,target = 30,30,1000

dp = [[0]*(target+1) for _ in range(d+1)]
for i in range(1,target+1):
    if i >f:
        break
    dp[1][i]=1
for i in range(1,d):
    flag = 0
    for j in range(1,target+1):
        if dp[i][j]:
            flag = 1
        if not dp[i][j] and flag:
            break
        for k in range(1,1+f):
            if j+k > target:
                break
            dp[i+1][j+k] += dp[i][j]
for i in dp:
    print(i)
print(dp[-1][-1]%1000000007)