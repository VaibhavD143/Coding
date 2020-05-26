def longestCommonSubsequence(A):
    dp = [[0]*(len(A)+1) for _ in range(len(A)+1)]
    
    for i in range(1,len(A)+1):
        for j in range(1,len(A)+1):
            if i!=j and A[i-1]==A[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return max(map(max,dp))