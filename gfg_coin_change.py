"""
https://practice.geeksforgeeks.org/problems/coin-change/0
"""
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    amt = int(input())
    dp = [0]*(amt+1)
    dp[0]=0
    for coin in coins:
        if coin<=amt:
            dp[coin] +=1
        for i in range(amt):
            if dp[i] != 0 and i+coin<=amt:
                dp[i+coin] += dp[i]
    print(dp[-1])