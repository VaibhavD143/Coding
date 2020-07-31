"""
Intution:
Find LCS of two strings, that is commong between both, now we are supposed to generate result
here row `i` represent string1,`j` represent string2
dp[i-1][j] == dp[i][j] means (i-1)th{as dp is 1-index} character is not part of LCS so add it
dp[i][j-1] == dp[i][j] means (j-1)th character is not part of LCS so add it to result
after loop i,j represents (i-1)st of string1 and (j-1)st of string2 is part of LCS so add only once
repeat
last is when we reach starting of any one of the string
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def findLCS(s1,s2):
            # print(s1,s2)
            dp = [[0]*(1+len(s2)) for _ in range(1+len(s1))]
            # parent = {}
            
            for i in range(1,len(dp)):
                for j in range(1,len(dp[0])):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            # for r in dp:
            #     print(r)
            res = []
            i=len(dp)-1
            j=len(dp[0])-1
            while i>0 and j>0:
                while i>0:
                    #append characters not part of LCS from s1
                    if dp[i-1][j]==dp[i][j]:
                        res.append(s1[i-1])
                        i-=1
                    else:
                        break
                while j>0:
                    #append characters not part of LCS from s2
                    if dp[i][j-1]==dp[i][j]:
                        res.append(s2[j-1])
                        j-=1
                    else:
                        break
                if i>0:
                    #both are part of LCS so only once
                    res.append(s1[i-1])
                i-=1
                j-=1
            while i>0:
                res.append(s1[i-1])
                i-=1
            while j>0:
                res.append(s2[j-1])
                j-=1
            return ''.join(res[::-1])
    
        return findLCS(str1,str2)