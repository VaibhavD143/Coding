#Look ib's solution
lst = [10,9,2,5,3,7,101,18]
lst = []
l = len(lst)
dp = [1]*l
for i in range(1,l):
    for j in range(i):
        if lst[j] < lst[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp,default=0))

