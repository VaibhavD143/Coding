"""
https://practice.geeksforgeeks.org/problems/edit-distance/0
https://leetcode.com/problems/edit-distance/
"""

def min_dist(str1,str2,ind1,ind2):
    global dp

    if ind1 == -1 or ind2 == -1:
        return abs(ind1-ind2)
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    if str1[ind1] == str2[ind2]:
        dp[ind1][ind2] = min_dist(str1,str2,ind1-1,ind2-1)
    else:
        dp[ind1][ind2] = min(min_dist(str1,str2,ind1-1,ind2-1),min_dist(str1,str2,ind1,ind2-1),min_dist(str1,str2,ind1-1,ind2))+1
    return dp[ind1][ind2]

for _ in range(int(input())):
    n,m = map(int,input().split())
    str1,str2 = input().split()
    dp = [[-1]*m for _ in range(n)]
    print(min_dist(str1,str2,len(str1)-1,len(str2)-1))