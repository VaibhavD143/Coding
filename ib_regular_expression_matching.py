class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        dp = [[False]*(len(A)+1) for _ in range(1+len(B))]
        
        dp[0][0]=True
        
        for i in range(1,len(dp)):
            if B[i-1] == '?' or B[i-1] == '*':
                dp[i][0]=True
            else:
                break
        jStart =0
        for i in range(1,len(dp)):
            #as 8 accepts empty sequence also, so start only from previous string character
            if B[i-1] != '*':
                jStart+=1
            
            #accepts any single character
            if B[i-1] == '?':
                for j in range(jStart,len(dp[0])):
                    dp[i][j] = dp[i-1][j-1]
            #once we find a true pattern, afterwards everything can be consumed in single *
            elif B[i-1] == "*":
                for j in range(jStart,len(dp[0])):
                    if dp[i-1][j]:
                        for k in range(j,len(dp[0])):
                            dp[i][k] = True
                        break
            #Normal character
            else:
                for j in range(jStart,len(dp[0])):
                    if B[i-1] == A[j-1] and dp[i-1][j-1]:
                        dp[i][j] = True
        return 1 if dp[-1][-1] else 0