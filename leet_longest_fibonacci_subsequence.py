"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
"""

lst = [1,2,3,4,5,6,7,8]
n = len(lst)
dp = [[0]*n for _ in range(n)]
ha = {}
for i in range(n):
    ha[lst[i]] = i
c_max = 0
for i in range(n-3,-1,-1):
    for j in range(i+1,n-1):
        # print('in')
        if ha.get(lst[i]+lst[j],-1) != -1:
            if dp[j][ha[lst[i]+lst[j]]] == 0:
                dp[i][j] = 3
            else:
                dp[i][j]= dp[j][ha[lst[i]+lst[j]]]+1
        if c_max<dp[i][j]:
            c_max = dp[i][j]
print(c_max)
for i in dp:
    print(i)
# print(dp)