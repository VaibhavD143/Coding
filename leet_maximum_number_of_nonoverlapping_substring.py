class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ha= {}
        string  =s
        for i,c in enumerate(s):
            if c in ha:
                ha[c][1] = i
            else:
                ha[c]=[i,i]
        intervals = []
        for i in range(26):
            ch = chr(i+ord('a'))
            if ch in ha:
                left,right = ha[ch]
                i = left
                while i<right:
                    right = max(right,ha[s[i]][1])
                    if ha[s[i]][0]<left:
                        right = None
                        break
                    i+=1
                if right!=None:
                    intervals.append((left,right))
        print(intervals)
        intervals= sorted(intervals,key=lambda item:(item[1],-item[0]))
        print(intervals)
        dp = [0]*(len(s)+1)
        dp[-1] = 0
        parent = [-1]*len(s)
        i=0
        for end in range(len(s)):
            if i<len(intervals) and intervals[i][1] == end:
                s,e = intervals[i]
                # print(s,e,dp[s-1],dp[end-1])
                if dp[s-1]+1>=dp[end-1]:
                    dp[end] = dp[s-1]+1
                    parent[end] = i
                else:
                    dp[end] = dp[end-1]
                i+=1
            else:
                dp[end] = dp[end-1]
        # print(dp)
        # print(parent)
        res = []
        i = len(string)-1
        while i>=0:
            while i>=0 and parent[i]==-1:
                i-=1
            while i>0 and dp[i-1]==dp[i]:
                i-=1
            if i>=0:
                s,e = intervals[parent[i]]
                res.append(string[s:e+1])
                i=s-1
        return res