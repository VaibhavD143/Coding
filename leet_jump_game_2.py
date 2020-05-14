lst = [2,3,1,1,4]
dp = [-1]*len(lst)
dp[0]=0
# for i in range(len(lst)):
#     for j in range(i+1,1+i+lst[i]):
#         if j>=len(lst):
#             break
#         if dp[j] == -1:
#             dp[j] = dp[i]+1
#         else:
#             dp[j] = min(dp[j],dp[i]+1)

for i in range(len(lst)):
    for j in range(min(len(lst)-1,i+lst[i]),i,-1):
        print(i,j)
        if dp[j] == -1:
            dp[j] = dp[i]+1
        elif dp[j] > dp[i]+1:
            dp[j] = dp[i]+1
        else:
            break
print(dp)