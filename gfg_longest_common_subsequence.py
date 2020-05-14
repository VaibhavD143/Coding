# https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0

for _ in range(int(input())):
    n,m = map(int,input().split())
    str1 = input()
    str2 = input()
    dp_table = [[0]*(n+1) for i in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            if str1[j] == str2[i]:
                dp_table[i+1][j+1] = 1 + dp_table[i][j]
            else:
                dp_table[i+1][j+1] = max(dp_table[i][j+1],dp_table[i+1][j])
    for x in dp_table:
        print(x)
