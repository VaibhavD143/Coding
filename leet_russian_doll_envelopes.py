class Solution:
    #Tle O(N**2)
    def maxEnvelopes1(self, lst: List[List[int]]) -> int:
        if len(lst)<2:
            return len(lst)
        def rec(prev):
            if dp[prev] != None:
                return dp[prev]
            cnt=0
            for i in range(prev,len(lst)):
                if lst[prev][0]>lst[i][0] and lst[prev][1]>lst[i][1]:
                    cnt = max(cnt,1+rec(i))
            dp[prev] = cnt
            return cnt
        lst.sort(reverse =True)
        dp = [None]*len(lst)
        res = 0
        for i in range(len(lst)):
            res = max(res,1+rec(i))
        return res
    #O(nlogn)
    #sort widh on increasing and for same width height decreasing, just find LIS 
    def maxEnvelopes(self, lst: List[List[int]]) -> int:
        if len(lst)<2:
            return len(lst)
        lst.sort(key = lambda i:(i[0],-i[1]))
        seq = []
        for _,e in enumerate(lst):
            ind = bisect.bisect_left(seq,e[1])
            if ind == len(seq):
                seq.append(e[1])
            else:
                seq[ind] = e[1]
        return len(seq)