from collections import defaultdict
class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        ha = defaultdict(list)
        for i,val in enumerate(A):
            ha[val].append(i)
        
        for key,val in ha.items():
            if len(val)<2:
                continue
            
            for key2,val2 in ha.items():
                if len(val2)<2:
                    continue
                if key == key2:
                    #>2 as AAA is valid, if not then change it to >3. so if any key with more than 2 incident is valid
                    if len(val2)>2:
                        return 1
                    else:
                        continue
                #Just considering left incident of key character and right most incidents of key2 character
                if val[0]<val2[-2] and val[1]<val2[-1]:
                    return 1
        return 0
    def longestCommonSubsequence(self,A):
        dp = [[0]*(len(A)+1) for _ in range(len(A)+1)]
        
        for i in range(1,len(A)+1):
            for j in range(1,len(A)+1):
                if i!=j and A[i-1]==A[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return 1 if max(map(max,dp))>=2 else 0