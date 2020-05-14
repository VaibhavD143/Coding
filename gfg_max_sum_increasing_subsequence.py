"""
https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

"""


for _ in range(int(input())):
    l = int(input())
    lst = list(map(int,input().split()))
    dp = [0]*l
    dp[0] = lst[0]
    for i in range(1,l):
        dp[i] = lst[i]
        for j in range(i):
            if lst[j] < lst[i] and dp[i] < dp[j]+lst[i]:
                dp[i] = dp[j]+lst[i]
    print(max(dp,default=0))