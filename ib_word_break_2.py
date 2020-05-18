"""
try to minimize loops if it is working on bigger length
"""
class Solution(object):
    def wordBreak(self, A, B):
        if not A:
            return []
        def giveSentences(A,ind,B,dp):
            if dp[ind] != -1:
                return dp[ind]
            sentences= []
            for word in B:
                if A[ind:ind+len(word)] == word:
                    if ind+len(word)==len(A):
                        sentences.append(word)
                    else:
                        results = giveSentences(A,ind+len(word),B,dp)
                        if results:
                            sentences+=[word+" "+res for res in results]
            dp[ind] = sentences if sentences else 0
            return dp[ind]
        dp= [-1 for _ in range(len(A))]
        B=list(set(B))
        giveSentences(A,0,B,dp)
        if not dp[0]:
            return []
        return dp[0]

#TLE in leetcode
class Solution:
    def wordBreak(self, A: str, B: List[str]) -> List[str]:
        def giveSentences(A,ind,B,dp):
            if ind==len(A):
                return [""]
            if dp[ind]:
                return dp[ind]
            sentences= []
            for word in B:
                if A[ind:ind+len(word)] == word:
                    results = giveSentences(A,ind+len(word),B,dp)
                    if results:
                        sentences+=[word+" "+res for res in results]
            dp[ind] = sentences if sentences else 0
            return dp[ind]
        dp= [[] for _ in range(len(A))]
        B=list(set(B))
        giveSentences(A,0,B,dp)
        if not dp[0]:
            return []
        res = [s.strip() for s in dp[0]]
        res.sort()
        return res