"""
https://leetcode.com/problems/coin-change/
"""
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
coins = [474,83,404,3]
amount = 2
dp = [amount+1]*(amount+1)
dp[0]=0
for i in range(amount+1):
    for coin in coins:
        if i+coin <= amount:
            dp[i+coin] = min(dp[i+coin],dp[i]+1)
    
print([dp[amount], -1][dp[amount] == amount+1])