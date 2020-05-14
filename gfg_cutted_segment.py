"""
https://practice.geeksforgeeks.org/problems/cutted-segments/0
"""

for _ in range(int(input())):
    n = int(input())
    curr = list(map(int,input().split()))

    coins = [0]*(n+1)
    coins[0] = 1
    for i in range(n+1):
        if coins[i]:
            for cur in curr:
                ind = i+cur
                if ind <= n:
                    if coins[i]+1>coins[ind]:
                        coins[ind] = coins[i]+1
    print(coins[-1]-1)
    