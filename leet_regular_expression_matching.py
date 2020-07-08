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
        #as we are missing on last character if it is not '*'
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
                    dp[i][j] = dp[i-1][j]   #zero occurance is also allowed
                
                    if regx[i-1][1] == '.' or regx[i-1][1] == s[j-1]:
                        dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                    
        return 1 if dp[-1][-1] else 0
        
        
#         string = list(s)
#         string.reverse()
#         tpat = []
#         i = len(p)-1
#         while i >=0:
#             if p[i] == '*':
#                 tpat.append('*'+p[i-1])
#                 i-=1
#             else:
#                 tpat.append(p[i])
#             i-=1
#         if len(string) == 0 and len(tpat) ==0:
#             return True
#         if len(tpat) == 0:
#             return False

#         dp = [[0]*(len(string)+1) for _ in range(1+len(tpat))]
#         dp[0][0] = 1
#         for i in range(1,len(tpat)+1):

#             if tpat[i-1] == '.':
#                 #mark yes if excluding this regx and current character it was True
#                 for j in range(1,len(string)+1):
#                     dp[i][j] = dp[i-1][j-1]
#             elif tpat[i-1][0] != '*':
#                 #if it is just normal character, mark yes if it matches with current string character and excluding this regx and character it was True
#                 for j in range(1,len(string)+1):
#                     if tpat[i-1] == string[j-1] and dp[i-1][j-1]:
#                         dp[i][j]=1
#             else:
#                 if tpat[i-1][1] == '.':
#                     """
#                     when regx is of type "*.", accept when True without regx(dp[i-1][j-1]), when True till previos string character(dp[i][j-1]),
#                     when it was True including current character as zero or more(dp[i-1][j])
#                     """
#                     dp[i][0] = dp[i-1][0]
#                     for j in range(1,len(string)+1):
#                         dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
#                 else:
#                     """
#                     when regx is of type "*b,*q", accept if True with current inclusion(dp[i-1][j]) as zero or more,
#                     when regx character matches with current string character 
#                     AND 
#                     it was True till previous character includinf regx or it was True exluding regx & string character
#                     """
#                     dp[i][0] = dp[i-1][0]
#                     for j in range(1,len(string)+1):
#                         if dp[i-1][j] or (string[j-1] == tpat[i-1][1] and (dp[i-1][j-1] or dp[i][j-1])): 
#                             dp[i][j] = 1
            
#         return dp[-1][-1]