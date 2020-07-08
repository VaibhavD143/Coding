"""
Intution:
Each bit is represented as a course index
dp[mask] = rec(mask) : minimum days to complete courses marked set in mask
possible : with current mask, set bits for courses whose pre-requisites are met
for current possible courses, try every possible susbset of size less or equal k,last loop is for that
"""
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        def countOne(n):
            if not n:
                return 0
            if n in ha:
                return ha[n]
            ha[n] = 1+countOne(n&(n-1))
            return ha[n]
        #VERSION-1
        # pre = [0]*n
        # for e in dependencies:
        #     pre[e[1]-1]+=(1<<(e[0]-1))
        
        #VERSION-2
        pre = [[] for _ in range(n)]
        for e in dependencies:
            pre[e[1]-1].append(e[0]-1)
        
        def rec(mask):
            if mask == 0:
                return 0
            
            if dp[mask]!=-1:
                return dp[mask]
        
            possible = 0    #Currently possible course bit set
            #VERSION-2
            for i in range(n):
                if mask&(1<<i):
                    flag = 1
                    for v in pre[i]:
                        if mask&(1<<v):
                            flag = 0
                    if flag:
                        possible+=(1<<i)
            #VERSION-1
            # done = mask^((1<<len(pre))-1)
            # for i,val in enumerate(pre):
            #     if mask&(1<<i) and val&done == val:
            #         possible +=(1<<i)
            
            submask = possible  #For iteration
            dp[mask] = 20
            while submask:
                if countOne(submask)<=k:
                    dp[mask] = min(dp[mask],1+rec(mask-submask))
                submask = (submask-1)&possible
            return dp[mask]
        
        dp = [-1]*(1<<n)
        ha = {}
        return rec((1<<n)-1)