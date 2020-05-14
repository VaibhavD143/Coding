
str1 = list("zxabcdezy")
str2 = list("111yzabcdezx")
ind1=len(str1)
ind2=len(str2)
# print(substring(str1,str2,ind1-1,ind2-1))
dp = [[0]*(ind2+1) for i in range(ind1+1)]
g_max = 0
e_ind1 = 0
e_ind2 = 0
for i in range(1,ind1+1):
    for j in range(1,ind2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            if dp[i][j] > g_max:
                g_max = dp[i][j]
                e_ind1 = i
                e_ind2 = j

print(g_max,e_ind1,e_ind2)