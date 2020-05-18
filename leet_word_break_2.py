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
