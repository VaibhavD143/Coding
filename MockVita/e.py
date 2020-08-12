n = int(input())
lst = list(map(int,input().split()))
lst = [-1]+lst+[-1]
dp = [[0]*len(lst) for _ in range(len(lst))]
for l in range(3,len(lst)+1):
    for i in range(0,len(lst)-l+1):
        j = i+l-1
        dp[i][j] = 0
        mx = max(lst[i],lst[j])
        mn = min(lst[i],lst[j])
        mn = 0 if mn == -1 else mn
        mx = 1 if mx == -1 else mx
        for k in range(i+1,j):
            q = dp[i][k]+dp[k][j]+(lst[k]*mx)+mn
            dp[i][j] = max(dp[i][j],q)
print(dp[0][len(lst)-1])

# def rec(l,r,lst):
#     if r-l<2:
#         return 0

#     if dp[l][r] != -1:
#         return dp[l][r]
#     res = 0
#     mx = max(lst[l],lst[r])
#     mn = min(lst[l],lst[r])
#     mn = 0 if mn == -1 else mn
#     mx = 1 if mx == -1 else mx
#     for i in range(l+1,r):
#         tres = rec(l,i,lst)+rec(i,r,lst)+(lst[i]*mx)+mn
#         res = max(res,tres)
#     # print(l,r,res)
#     dp[l][r] = res
#     return res
# # lst = [0,2,2,0]
# for (L=2; L<n; L++) 
# { 
#     for (i=1; i<n-L+1; i++) 
#     { 
#         j = i+L-1; 
#         if(j == n) continue; 
#         m[i][j] = Integer.MAX_VALUE; 
#         for (k=i; k<=j-1; k++) 
#         { 
#             // q = cost/scalar multiplications 
#             q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]; 
#             if (q < m[i][j]) 
#                 m[i][j] = q; 
#         } 
#     } 
# } 
# return m[1][n-1]; 
# # print(rec(0,len(lst)-1,lst))
# lst = [-1,2,2,-1]

# for i in range(1,len(lst)-1):
#     dp[i][i] = lst[i-1]

# for r in dp:
#     print(r)