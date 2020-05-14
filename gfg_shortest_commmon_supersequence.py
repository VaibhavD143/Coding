"""
https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0
"""

for _ in range(int(input())):
    s1,s2 = input().split()
    if len(s1)<len(s2):
        s1,s2 = s2,s1
    
    dp = [[0]*(len(s1)+1) for _ in range(1+len(s2))]
    for i in range(len(s2)+1):
        dp[i][0] = i
    
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]+1)
    print(dp[-1][-1]+len(s1))