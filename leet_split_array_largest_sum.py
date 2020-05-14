lst = [7,2,5,10,8]
m = 4
def pp(matrix):
    for row in matrix:
        print(row)
dp = [[0]*len(lst) for _ in range(m)]
dp[0][-1] = lst[-1]

for i in range(len(lst)-2,-1,-1):
    dp[0][i] = dp[0][i+1]+lst[i]
for i in range(1,len(lst)):
    dp[1][i] = dp[1][i-1]+lst[i-1]

for i in range(2,m):
    for j in range(i,len(lst)-(m-i-1)):
            minVal = float('inf')
            for k in range(i-1,j):
                minVal = min(minVal,max(dp[i-1][k],dp[1][j]-dp[1][k]))
            dp[i][j] = minVal
res = float('inf')
for i in range(m-1,len(lst)):
    res = min(res,max(dp[0][i],dp[m-1][i]))
print(res)