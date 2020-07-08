class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0  and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        regx = []
        i=1
        while i<len(p):
            if p[i]=='*':
                regx.append('*'+p[i-1])
                i+=1
            else:
                regx.append(p[i-1])
            i+=1
        if p[-1] != '*':
            regx.append(p[-1])
        dp=[[False]*(1+len(s)) for _ in range(1+len(regx))]
        
        dp[0][0]=True
        for i in range(1,len(dp)):
            if regx[i-1][0]=='*':
                dp[i][0]=True
            else:
                break
        # print(regx)
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                if regx[i-1] == '.' or regx[i-1] == s[j-1]: 
                    dp[i][j] = dp[i-1][j-1]
                
                elif regx[i-1][0] == '*':
                    dp[i][j] = dp[i-1][j]
                
                    if regx[i-1][1] == '.' or regx[i-1][1] == s[j-1]:
                        dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                    
        return 1 if dp[-1][-1] else 0
        
