"""
https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
"""

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    sum_nums = sum(nums)
    if sum_nums&1:
        print("NO")
        continue
    k = sum_nums//2
    dp = [0]*(k+1)
    dp[0]=1
    for num in nums:
        for j in range(k-num,-1,-1):
            if dp[j]:
                dp[j+num]=1
        if dp[-1]:
            break
    # print(dp)
    if dp[-1]:
        print("YES")
    else:
        print("NO")

